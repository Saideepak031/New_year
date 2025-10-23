// a minimal JS calendar renderer. It will render the given month/year into #calendar
function renderCalendar(containerId, year, month) {
  const container = document.getElementById(containerId);
  const date = new Date(year, month, 1);
  const monthNames = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  let html = '<div class="calendar card">';
  html += `<h3>${monthNames[month]} ${year}</h3>`;
  html += '<table style="width:100%;">';
  html += '<tr><th>Sun</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th><th>Sat</th></tr>';
  html += '<tr>';
  // blanks
  for(let i=0;i<date.getDay();i++){ html += '<td></td>'; }
  while(date.getMonth()===month){
    html += `<td>${date.getDate()}</td>`;
    if(date.getDay()===6) html += '</tr><tr>';
    date.setDate(date.getDate()+1);
  }
  html += '</tr></table>';
  html += '</div>';
  container.innerHTML = html;
}

// provide navigation
function initCalendar(containerId, startYear=2026, startMonth=0) {
  let y = startYear, m = startMonth;
  const c = document.getElementById(containerId + '-nav');
  c.querySelector('.prev').addEventListener('click', ()=>{ m--; if(m<0){ m=11; y--; } renderCalendar(containerId,y,m); });
  c.querySelector('.next').addEventListener('click', ()=>{ m++; if(m>11){ m=0; y++; } renderCalendar(containerId,y,m); });
  renderCalendar(containerId,y,m);
}