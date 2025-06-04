//제출 이벤트
const fomr = document.getElementById('form')
form.addEventListener('submit', function (e) {
    //제출 입력 값 참조
    e.preventDefault()
    let id = e.target.id.value
    let pw1 = e.target.pw1.value
    let pw2 = e.target.pw2.value
    let name = e.target.name.value
    let phone = e.target.phone.value
    let position = e.target.position.value
    let gender = e.target.gender.value
    let email = e.target.email.value
    let intro = e.target.intro.value

    //에러 감지
    if (id.length < 6) {
        alert('아이디가 너무 짧습니다. 6자 이상 입력하세요.')
        return
    }

    if (pw1 !== pw2) {
        alert('비밀호가 일치하지 않아요.')
        return
    }

    //가입 환영 인사
    document.body.innerHTML = ""
    document.write(`<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>회원가입 양식</title>
    <link rel="stylesheet" href="join.css">
    </head>
    <body>
    <div id="container"><div class='next'>${id}님 환영합니다.<br>
    회원 가입 시 입력학신 내역은 다음과 같습니다.<br>
    아이디 : ${id}<br>
    이름 : ${name}<br>
    전화번호 : ${phone}<br>
    원하는 직무 : ${position}</div></div></body>
    `)
    })