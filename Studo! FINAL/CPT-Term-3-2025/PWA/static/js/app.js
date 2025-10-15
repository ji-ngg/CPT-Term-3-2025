document.addEventListener('DOMContentLoaded', () => {
  // popup container
  const popupContainer = document.getElementById('popup-container');

  const openMusic = document.getElementById('open-music-settings');
  if (openMusic) openMusic.addEventListener('click', async () => {
    const opts = await fetch('/options').then(r=>r.json());
    openMusicPopup(opts);
  });

  function openMusicPopup(opts){
    popupContainer.innerHTML = '';
    const el = document.createElement('div');
    el.className = 'popup';
    el.innerHTML = `
      <button class="close" id="close-music">&times;</button>
      <h4>music + alarm settings</h4>
      <div class="section"><h5>choose alarm sound</h5><div id="alarm-list" class="option-grid"></div></div>
      <div class="section"><h5>choose background</h5><div id="bg-list" class="option-grid"></div></div>
      <div class="actions"><button id="save-music-settings" class="btn">save</button></div>
    `;
    popupContainer.appendChild(el);

    let currentSample = null;
    const alarmList = el.querySelector('#alarm-list');
    opts.alarms.forEach(a => {
      const b = document.createElement('button');
      b.textContent = a.label;
      b.dataset.id = a.id;
      b.addEventListener('click', () => {
        if (currentSample) currentSample.pause();
        currentSample = new Audio('/static/sounds/' + a.id);
        currentSample.loop = false;
        currentSample.play();
        setTimeout(() => {currentSample.pause();}, 3000);
        el.querySelectorAll('#alarm-list button').forEach(x=>x.classList.remove('selected'));
        b.classList.add('selected');
      });
      alarmList.appendChild(b);
    });

    const bgList = el.querySelector('#bg-list');
    opts.backgrounds.forEach(bg => {
      const b = document.createElement('button');
      b.className = 'bg-option';
      b.style.background = bg.id;
      b.dataset.id = bg.id;
      b.addEventListener('click', () => {
        document.body.style.background = bg.id;
        el.querySelectorAll('#bg-list button').forEach(x=>x.classList.remove('selected'));
        b.classList.add('selected');
      });
      bgList.appendChild(b);
    });

    el.querySelector('#close-music').addEventListener('click', ()=> popupContainer.innerHTML = '');

    el.querySelector('#save-music-settings').addEventListener('click', async () => {
      const chosenAlarm = el.querySelector('#alarm-list .selected')?.dataset.id || 'alarm_duck.mp3';
      const chosenBg = el.querySelector('#bg-list .selected')?.dataset.id || '#edf2f4';
      await fetch('/save_settings', {method:'POST', headers:{'content-type':'application/json'}, body:JSON.stringify({chosen_bg:chosenBg, chosen_alarm:chosenAlarm, chosen_bgm:null})});
      popupContainer.innerHTML = '';
      alert('saved settings');
    });
  }

const openSite = document.getElementById('open-site-settings');
  if (openSite) openSite.addEventListener('click', async () => {
    popupContainer.innerHTML = '';
    const el = document.createElement('div');
    el.className='popup';
    el.innerHTML=`
      <button class="close" id="close-settings">&times;</button>
      <div class="section"><h5>feedback</h5><textarea id="feedback" rows="4" placeholder="How can we improve the site?"></textarea></div>
      <div class="actions"><button id="save-site-settings" class="btn">save</button></div>
    `;
    
    popupContainer.appendChild(el);
    
    el.querySelector('#close-settings').addEventListener('click', ()=> popupContainer.innerHTML = '');
    el.querySelector('#save-site-settings').addEventListener('click', async ()=>{
      const feedback = el.querySelector('#feedback').value;
      if (feedback.trim()) {
        console.log('Feedback submitted:', feedback);
        alert('Thank you for your feedback!');
      } else {
        alert('Please enter some feedback before saving.');
      }
      popupContainer.innerHTML = '';
    });
  });

});

