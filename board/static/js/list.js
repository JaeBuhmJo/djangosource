document.querySelector("ul.pagination").addEventListener("click", e => {
  e.preventDefault();
  if (e.target.tagName === "A") {
    const page = e.target.getAttribute("href");
    console.log(page);
  }
});
