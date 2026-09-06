/* TrackLink — site behaviour.
   Vanilla JS, no dependencies. Progressive enhancement only:
   the site works fully without it. */

(function () {
  "use strict";

  /* Footer year */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  /* Mobile nav toggle */
  var toggle = document.querySelector(".nav__toggle");
  var links = document.getElementById("primary-nav");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    // Close menu when a link is chosen (mobile)
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A" && links.classList.contains("is-open")) {
        links.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* Screenshot lightbox.
     Each .shot__zoom is already an <a> to the full-resolution image, so with
     this script absent (or failed) a click simply opens that file. Here we
     intercept the click and show it over a dimmed backdrop instead. */
  var zooms = document.querySelectorAll(".shot__zoom");
  if (zooms.length) {
    var box = null;
    var lastFocus = null;

    function buildBox() {
      var el = document.createElement("div");
      el.className = "lightbox";
      el.setAttribute("role", "dialog");
      el.setAttribute("aria-modal", "true");
      el.hidden = true;
      el.innerHTML =
        '<button type="button" class="lightbox__close" aria-label="Close image">' +
          '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
          'stroke-width="2.2" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" stroke-linecap="round"/></svg>' +
        '</button><figure class="lightbox__fig"></figure>';

      // A click on the backdrop closes; a click on the image itself does not.
      el.addEventListener("click", function (e) {
        if (e.target === el || el.querySelector(".lightbox__close").contains(e.target)) closeBox();
      });
      document.body.appendChild(el);
      return el;
    }

    function openBox(trigger) {
      if (!box) box = buildBox();
      lastFocus = document.activeElement;

      var img = trigger.querySelector("img");
      var webp = trigger.getAttribute("data-webp");
      var title = trigger.getAttribute("data-title") || "";
      var alt = img ? img.getAttribute("alt") || "" : title;

      // Rebuilt each time: a <source> added after the <img> has already been
      // resolved would be ignored by the browser.
      var pic = document.createElement("picture");
      if (webp) {
        var src = document.createElement("source");
        src.setAttribute("srcset", webp);
        src.setAttribute("type", "image/webp");
        pic.appendChild(src);
      }
      var full = document.createElement("img");
      full.setAttribute("src", trigger.getAttribute("href"));
      full.setAttribute("alt", alt);
      if (img) {
        full.setAttribute("width", img.getAttribute("width"));
        full.setAttribute("height", img.getAttribute("height"));
      }
      pic.appendChild(full);

      var cap = document.createElement("figcaption");
      cap.innerHTML = title;

      var fig = box.querySelector(".lightbox__fig");
      fig.innerHTML = "";
      fig.appendChild(pic);
      fig.appendChild(cap);

      box.setAttribute("aria-label", cap.textContent || "Product screenshot");
      box.hidden = false;
      document.body.classList.add("has-lightbox");
      // Let the browser paint the hidden state first so the fade actually runs.
      requestAnimationFrame(function () { box.classList.add("is-open"); });
      box.querySelector(".lightbox__close").focus();
    }

    function closeBox() {
      if (!box || box.hidden) return;
      box.classList.remove("is-open");
      box.hidden = true;
      document.body.classList.remove("has-lightbox");
      if (lastFocus && lastFocus.focus) lastFocus.focus();
      lastFocus = null;
    }

    document.addEventListener("keydown", function (e) {
      if (!box || box.hidden) return;
      if (e.key === "Escape") { closeBox(); return; }
      // The close button is the only control in here, so keep Tab on it.
      if (e.key === "Tab") {
        e.preventDefault();
        box.querySelector(".lightbox__close").focus();
      }
    });

    Array.prototype.forEach.call(zooms, function (a) {
      a.addEventListener("click", function (e) {
        // Leave modified clicks alone so "open in new tab" still works.
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button) return;
        e.preventDefault();
        openBox(a);
      });
    });
  }
})();
