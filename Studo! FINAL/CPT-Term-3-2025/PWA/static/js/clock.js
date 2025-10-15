
document.addEventListener('DOMContentLoaded', () => {

  const clockEl = document.getElementById('clock-time');
  if (clockEl) {
    function updateClock(){
      const now = new Date();
      let hrs = now.getHours();
      const ampm = hrs >= 12 ? 'pm' : 'am';
      hrs = hrs % 12; if (hrs === 0) hrs = 12;
      let mins = now.getMinutes().toString().padStart(2,'0');
      clockEl.textContent = hrs + ":" + mins + ampm;
    }
    updateClock();
    setInterval(updateClock, 1000);
  }


  const pomTimeEl = document.getElementById('pom-time');
  if (pomTimeEl) {
    const alarm = document.getElementById('alarm-audio');
    const bgm = document.getElementById('bgm-audio');
    let timer = null;
    let alarmTimeout = null;
    let total = 25*60;

    function stopAlarm() {
      if (alarm) {
        alarm.pause();
        alarm.currentTime = 0;
      }
      if (alarmTimeout) {
        clearTimeout(alarmTimeout);
        alarmTimeout = null;
      }
    }

    function setMode(mode){
      if (mode === 'work') total = 25*60;
      if (mode === 'short') total = 5*60;
      if (mode === 'long') total = 15*60;
      renderPom();
    }

    function renderPom(){
      let m = Math.floor(total/60);
      let s = total%60;
      pomTimeEl.textContent = `${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
    }

    function tick(){
      if (total>0){
        total--;
        renderPom();
      } else {
        clearInterval(timer);
        timer = null;
        if (alarm) {
          alarm.currentTime = 0;
          alarm.play();
          alarmTimeout = setTimeout(stopAlarm, 5000); 
        }
        document.getElementById('pom-message').textContent = `you can do it, ${window.USER.first_name || 'friend'}!`;
        fetch('/record_timer', {method:'POST', headers:{'content-type':'application/json'}, body:JSON.stringify({mode:'pomodoro', duration:25})});
      }
    }

    document.getElementById('pom-mode').addEventListener('change', e => setMode(e.target.value));
    document.getElementById('pom-start').addEventListener('click', () => {
      if (!timer) {
        timer = setInterval(tick, 1000);
        if (bgm) bgm.play();
      }
    });
    document.getElementById('pom-stop').addEventListener('click', () => {
      if (timer) { clearInterval(timer); timer = null; if (bgm) bgm.pause(); }
    });
    document.getElementById('pom-reset').addEventListener('click', () => {
      clearInterval(timer); timer = null;
      setMode(document.getElementById('pom-mode').value);
      if (bgm) bgm.pause();
      stopAlarm(); 
      document.getElementById('pom-message').textContent = '';
    });
    setMode('work');
  }


  const countdown = document.getElementById('countdown-time');
  if (countdown) {
    const alarm = document.getElementById('timer-alarm');
    const bgm = document.getElementById('timer-bgm');
    let running = false;
    let remain = 21*60;
    let alarmTimeout = null;

    function stopAlarm() {
      if (alarm) {
        alarm.pause();
        alarm.currentTime = 0;
      }
      if (alarmTimeout) {
        clearTimeout(alarmTimeout);
        alarmTimeout = null;
      }
    }

    function render(){
      const h = Math.floor(remain/3600);
      const m = Math.floor((remain%3600)/60);
      const s = remain%60;
      countdown.textContent = `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
    }

    function tick(){
      if (remain > 0){
        remain--;
        render();
      } else {
        clearInterval(window._timerInt);
        running = false;
        if (alarm) {
          alarm.currentTime = 0;
          alarm.play();
          alarmTimeout = setTimeout(stopAlarm, 5000); 
        }
        fetch('/record_timer', {method:'POST', headers:{'content-type':'application/json'}, body:JSON.stringify({mode:'timer', duration:0})});
      }
    }

    document.getElementById('timer-start').addEventListener('click', () => {
      if (!running) {
        const mins = parseInt(document.getElementById('timer-min').value) || 0;
        const secs = parseInt(document.getElementById('timer-sec').value) || 0;
        remain = mins*60 + secs;
        render();
        window._timerInt = setInterval(tick, 1000);
        running = true;
        if (bgm) bgm.play();
      } else {
        clearInterval(window._timerInt);
        running = false;
        if (bgm) bgm.pause();
      }
    });

    document.getElementById('timer-reset').addEventListener('click', () => {
      clearInterval(window._timerInt);
      running = false;
      const mins = parseInt(document.getElementById('timer-min').value) || 0;
      const secs = parseInt(document.getElementById('timer-sec').value) || 0;
      remain = mins*60 + secs;
      render();
      if (bgm) {
        bgm.pause();
        bgm.currentTime = 0;
      }
      stopAlarm(); 
    });

    render();
  }
});
