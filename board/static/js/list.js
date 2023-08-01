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

// 정렬 기준 변화 시 값을 가져와서
// page=1로 변경
// actionForm의 sort 값 변경한 후 actionForm 전송
const select = document.querySelector("select.so");

select.addEventListener("change", e => {
  actionForm.querySelector("#page").value = 1;
  actionForm.querySelector("#sort").value = select.value;
  actionForm.submit();
});

// 제목 클릭 시
// a태그 중지, href값 가져오기
// actionForm의 action값을 가져온 href로 변경 후 actionForm submit
const subjects = document.querySelectorAll("td>a");
subjects.forEach(title => {
  title.addEventListener("click", e => {
    e.preventDefault();
    const href = e.target.href;
    actionForm.action = href;
    actionForm.submit();
  });
});
