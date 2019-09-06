////var Logbtn = $('#btn-login')
//
//function loginProcess(data){
//    $.ajax({
//        url:'/infolist/api/login',
//        type:'POST',
//        data:JSON.stringify(data),
//        contentType:'application/json',
//        success:function(data,textStatus,jqXHR){
//            var session_token = data["session_token"]
//            window.sessionStorage["session_token"]=data["session_token"]
//            window.location.href = "infolist/mail-conf"
//        }
//    })
//}
//
//$(document).ready(functon()
//{
//    $('#btn-login').on('click', function (e) {
//        var data = {};
//        data['username'] = $('#username').val();
//        data['password'] = $('#password').val();
//        loginProcess(data)
//    })
//})