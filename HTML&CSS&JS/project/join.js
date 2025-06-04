//제출 이벤트
const form = document.getElementById('form')
form.addEventListener('submit', function (e) {
    //제출 입력 값 참조
    e.preventDefault()
    let id = e.target.id.value
    let pw1 = e.target.pw1.value
    let pw2 = e.target.pw2.value
    let name = e.target.name.value
    let phone = e.target.phone.value
    let gender = e.target.gender.value
    let email = e.target.email.value

    //에러 감지
    if (id.length < 6) {
        alert('아이디가 너무 짧습니다. 6자 이상 입력하세요.')
        return
    }

    if (pw1 !== pw2) {
        alert('비밀번호가 일치하지 않아요.')
        return
    }

    //가입 환영 인사
    alert(`${id}님 환영합니다.
회원 가입 시 입력학신 내역은 다음과 같습니다.
아이디 : ${id}
이름 : ${name}
전화번호 : ${phone}`)
})