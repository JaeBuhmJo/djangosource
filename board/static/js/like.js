// 좋아요 이미지 클릭 시

const like_button = document.querySelector(".recommend button");

like_button.addEventListener("click", e => {
  e.preventDefault();
  const post_id = like_button.dataset.id;
  fetch("/blogs/likes/" + post_id).then(response => {
    if (!response.ok) {
      throw new Error(" 에러 발생 ");
    }
    return response.json();
  }).then(data => {
    document.querySelector(".recommend .like").classList.toggle("disabled");
    document.querySelector(".recommend .dislike").classList.toggle("disabled");
    document.querySelector(".like_count").innerHTML = data["likes"];
  }).catch(error => console.log(error));
});
