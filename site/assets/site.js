(function () {
  // Mobile menu
  var btn = document.getElementById('menuBtn'), nav = document.getElementById('nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
  }

  // Customer-type tabs (home page)
  var tabs = [].slice.call(document.querySelectorAll('.tab'));
  function select(t) {
    tabs.forEach(function (x) {
      var on = x === t;
      x.setAttribute('aria-selected', on);
      x.tabIndex = on ? 0 : -1;
      document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
    });
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { select(t); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      var n = tabs[(i + d + tabs.length) % tabs.length];
      select(n); n.focus(); e.preventDefault();
    });
  });

  // Pre-select a service in the quote form from contact.html#slug
  var form = document.getElementById('quoteForm');
  if (!form) return;
  try {
    var want = location.hash.slice(1);
    if (want) {
      var opt = form.querySelector('#f-svc option[data-slug="' + want + '"]');
      if (opt) opt.selected = true;
    }
  } catch (e) {}

  // Quote form. On the live domain it submits normally (Netlify Forms).
  // Anywhere else (local file, preview) it shows a message instead.
  var msg = document.getElementById('formMsg');
  var live = /(^|\.)nationalelectrical\.uk$/.test(location.hostname) || /\.netlify\.app$/.test(location.hostname);
  form.addEventListener('submit', function (e) {
    var name = form.elements['name'].value.trim();
    var phone = form.elements['phone'].value.trim();
    if (!name || !phone) {
      e.preventDefault();
      msg.hidden = false;
      msg.textContent = 'Please add your name and phone number so we can call you back.';
      return;
    }
    if (!live) {
      e.preventDefault();
      msg.hidden = false;
      msg.textContent = 'Thanks ' + name + '. This is a preview, so nothing was sent. On nationalelectrical.uk this form will email your enquiry to the team.';
    }
  });
})();
