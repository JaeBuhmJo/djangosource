const deleteAll = document.querySelectorAll(".delete");

deleteAll.forEach(item => {
  item.addEventListener("click", e => {
    e.preventDefault();
    if (confirm("정말로 삭제하시겠습니까?")) {
      location.href = e.target.href;
    }
  });
});

const recommemdAll = document.querySelectorAll(".recommend");
recommemdAll.forEach(item => {
  item.addEventListener("click", e => {
    e.preventDefault();
    if (confirm("정말로 추천하시겠습니까?")) {
      location.href = e.target.href;
    }
  });
});
