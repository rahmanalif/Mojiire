document.addEventListener('DOMContentLoaded', () => {
  /* ---------- HOOKS ---------- */
  const calendarDays = document.getElementById('calendar-days');
  const monthYear    = document.getElementById('month-year');
  const prevBtn      = document.getElementById('prev-month');
  const nextBtn      = document.getElementById('next-month');

  if (!calendarDays || !monthYear || !prevBtn || !nextBtn) {
    console.error('Calendar: required elements not found — check the IDs.');
    return;
  }

  /* ---------- CORE ---------- */
  const monthNames = [
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
  ];
  let currentDate = new Date();

  function renderCalendar(date){
    const year        = date.getFullYear();
    const month       = date.getMonth();
    const firstDay    = new Date(year, month, 1).getDay();       // 0-6
    const daysInMonth = new Date(year, month + 1, 0).getDate();  // 28-31

    monthYear.textContent = `${monthNames[month]} ${year}`;
    calendarDays.innerHTML = '';                       // clear grid

    /* blank cells before day 1 */
    for (let i = 0; i < firstDay; i++) {
      calendarDays.appendChild(document.createElement('div'));
    }
    /* actual day cells */
    for (let day = 1; day <= daysInMonth; day++) {
      const cell  = document.createElement('div');
      const today = new Date();

      if (
        day   === today.getDate()  &&
        month === today.getMonth() &&
        year  === today.getFullYear()
      ){
        cell.classList.add('today');
      }

      cell.textContent = day;
      cell.addEventListener('click', () => {
        alert(`You clicked on ${monthNames[month]} ${day}, ${year}`);
      });

      calendarDays.appendChild(cell);
    }
  }

  /* ---------- NAV ---------- */
  prevBtn.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar(currentDate);
  });
  nextBtn.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar(currentDate);
  });

  /* ---------- INIT ---------- */
  renderCalendar(currentDate);
});
