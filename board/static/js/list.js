document.querySelector("ul.pagination").addEventListener("click", e => {
  e.preventDefault();
  if (e.target.tagName === "A") {
    const href = e.target.getAttribute("href");
    document.querySelector("#page").value = href;
    document.querySelector("#actionForm").submit();
  }
});
