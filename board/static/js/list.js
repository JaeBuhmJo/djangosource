document.querySelector("ul.pagination").addEventListener("click", e => {
  e.preventDefault();
  if (e.target.tagName === "A") {
    const href = e.target.getAttribute("href");
    document.querySelector("#page").value = href;
    document.querySelector("#actionForm").submit();
  }
});

// 찾기 버튼 클릭 시
// 검색어 입력 여부 확인
//검색어가 없으면 알러트
//있으면 액션폼 밸류 변경 후 서브밋
const actionForm = document.querySelector("#actionForm");

document.querySelector("#btn_search").addEventListener("click", e => {
  e.preventDefault();
  const topKeyword = document.querySelector("#top_keyword");
  if (topKeyword.value == "") {
    alert("검색어를 입력해주세요");
    topKeyword.focus();
    return;
  }
  actionForm.querySelector("#keyword").value = topKeyword.value;
  actionForm.submit();
});
