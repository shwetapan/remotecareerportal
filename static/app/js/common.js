//var defaultUrl="http://localhost:8888/";

var defaultUrl="http://120.24.48.43:8888/";

function getSuccessMsg(msg) {
    $.message({
        message:msg,
        type:'success',
        duration:'3000'
    });
}

function getInfoMsg(msg) {
    $.message({
        message:msg,
        type:'info',
        duration:'3000'
    });
}

function getFailMsg(msg) {
    $.message({
        message:msg,
        type:'error',
        duration:'3000'
    });
}

function getValue(id) {
    var value = $("#" + id).val();
    if (value != null) {
        if (value != "") {
            return value;
        }
    }
    return null;
}

function getSelectText(id){
    var text = $("#" + id + " option:selected").text();
    if (text != null) {
        if (text != "") {
            return text;
        }
    }
    return null;
}

function getSelectValue(id){
    var value = $("#" + id + " option:selected").val();
    if (value != null) {
        if (value != "") {
            return value;
        }
    }
    return null;
}

function error(data) {
    getFailMsg("服务器异常");
}



/**
 * 判断是不是邮箱格式
 * @param {} email 
 */
function checkEmail(email) {
    var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    if (reg.test(email)) {
        return true;
    } else {
        getInfoMsg("请输入正确格式的邮箱！！！");
        return false;
    }
}

/**
 * 检查数字的长度
 * @param {*} str 
 * @param {*} len 
 */
function checkStringLength(str,len) {
    var reg = /^[0-9]{6}$/;
    if (reg.test(str)) {
        return true;
    } else {
        getInfoMsg("请输入六位数字验证码！！！");
        return false;
    }
}

function checkPhone(phone) {
    var reg = /^1(3|4|5|6|7|8|9)\d{9}$/;
    if (reg.test(phone)) {
        return true;
    } else {
        getInfoMsg("请输入正确电话号码！！！");
        return false;
    }
}

function sleep(n) {
    var start = new Date().getTime();
    //  console.log('休眠前：' + start);
    while (true) {
        if (new Date().getTime() - start > n) {
            break;
        }
    }
}

// 加载导航条
function loadTopNav() {
    //$("#topnav").empty();
    $.ajax({
        type:"get",
        url:"topnav.html",
        async:false,
        success:function(data){
            $("#topnav").append(data);
        }
    });
}

// 加载页底导航条
function loadFootNav() {
    $(".footer footer-bar").empty();
    $.ajax({
        type:"get",
        url:"footer.html",
        async:false,
        success:function(data){
            $(".footer footer-bar").html(data);
        }
    });
}

/**
 * 注销
 */
function logout() {
    Notiflix.Confirm.Show(
        '确认',
        '您确定要注销吗？',
        '确定',
        '取消',
        function(){ 
            localStorage.clear();
            Notiflix.Report.Success(
                '注销成功',
                ' ',
                '关闭',
                function () {
                    location.reload();
                }
            );
        },function(){ 
            // No button callbackalert('If you say so...');
        }
    );
}


function jump() {
    Notiflix.Report.Info(
        '请先登录后再尝试!!!',
        ' ',
        '关闭',
        function () {
            window.location.href = "login.html";
        }
    )
    return;
}

function nav() {
    var token = localStorage.getItem("token");
    if (token == null) {
        $("#user-menu").html('<a href="login.html">登录|注册</a></li>');
    }
}

function getFileName(){
    //
    upload();
}

function getUser() {
    var user = JSON.parse(localStorage.getItem("userInfo"));
    return user;
}

function setName() {
    var user = getUser();
    if (user != null) {
        $("#job-user-name").html(user.userName);
    } else {
        $("#user-menu").html('<a href="login.html">登录|注册</a>');
    }
}

//文件上传
function upload(){
    var token = localStorage.getItem("token");
    token = token.substring(1, token.length - 1);
    $.ajax({
        url: defaultUrl + "base/upload",
        type: 'POST',
        cache: false,
        data: new FormData($('#ff')[0]),
        processData: false,
        contentType: false,
        dataType:"json",
        headers:{"token":token},
        success : function(data) {
            if (data.code == 200) {
                $("#head-image").attr("src", data.data);
                $("#icon").val(data.data); 
                getSuccessMsg("上传成功");
            } else {
                getFailMsg(data.message);
            }
        },error :function(data){
            getFailMsg(data.message);
        }
    });
} 


// 根据社会信用id获取公司信息
function getCompanyByUniformCreditCode() {
    var uniformCreditCode = getValue("uniformCreditCode");
    if (uniformCreditCode == null || uniformCreditCode == true || uniformCreditCode == "") {
        getInfoMsg("请先输入社会信用编码");
        return;
    }
    var company;
    var flag;
    $.ajax({
        type:"GET",
        async:false,
        url:defaultUrl + "company/getCompanyByUniformCreditCode",
        dataType:"json",
        data:{
            "uniformCreditCode":uniformCreditCode
        },
        success:function(data) {
            if (data.code == 200) {
                company = data.data.company;
                if (company != null) {
                    flag = true;
                    $("#companyName").val(company.name);
                    $("#companyNo").val(company.companyNo);
                    getSuccessMsg("已检测");
                } else {
                    getInfoMsg("该站点不存在该公司信息");
                }
            }
        }
    });
    if (flag) {
        return company;
    } else {
        return null;
    }
    
}
{/* <li class="page-item disabled">
    <a class="page-link" href="#" tabindex="-1" aria-disabled="true">
        <i class="mdi mdi-chevron-double-left f-15"></i>
    </a>
</li>
<li class="page-item active"><a class="page-link" href="#">1</a></li>
<li class="page-item"><a class="page-link" href="#">2</a></li>
<li class="page-item"><a class="page-link" href="#">3</a></li>
<li class="page-item"><a class="page-link" href="#">4</a></li>
<li class="page-item">
    <a class="page-link" href="#">
        <i class="mdi mdi-chevron-double-right f-15"></i>
    </a>
</li> */}
function generatePaginaionNav(pagination) {
    $("#pagination").empty();
    
    var item = "";
    var max = 1;
    var currentPage = pagination.currentPage;
    var total = pagination.total;
    var pageSize = pagination.pageSize;
    // 计算最大页码
    max = total % pageSize == 0 ? parseInt(total / pageSize) : parseInt(total / pageSize) + 1;
    var totalPage = pagination.currentPage + 3 > max ? max : currentPage + 3;
    item = item + '<li class="page-item">'+
                        '<a class="page-link" href="javascript:getInfoByPage('+ (currentPage - 1) +',' + max + ')" tabindex="-1" aria-disabled="true">'+
                            '<i class="mdi mdi-chevron-double-left f-15"></i>'+
                        '</a>'+
                    '</li>';
    item = item + '<li class="page-item active"><a class="page-link" href="javascript:getInfoByPage('+ currentPage +',' + max + ')">'+currentPage+'</a></li>';
    for (var i = currentPage + 1; i <= totalPage; i++) {
        item = item + '<li class="page-item"><a class="page-link" href="javascript:getInfoByPage('+ i +',' + max + ')">' + i + '</a></li>';
    }
    item = item + '<li class="page-item">'+
                        '<a class="page-link" href="javascript:getInfoByPage('+ (currentPage + 1) +',' + max + ')" tabindex="-1" aria-disabled="true">'+
                            '<i class="mdi mdi-chevron-double-right f-15"></i>'+
                        '</a>'+
                    '</li>';
    $("#pagination").append(item);
}

function getState(state) {
    state = parseInt(state);
    if (state == 0) {
        return "待处理";
    } else if (state == 1) {
        return "初筛通过";
    } else if (state == 2) {
        return "初筛不通过";
    } else {
        return "";
    }
}

function getInfoByPage(pageNum,max) {
    if (pageNum <= 0) {
        Notiflix.Report.Info(
            '不能再往前了!!!',
            ' ',
            '关闭'
        )
        return;
    }
    if (pageNum > max) {
        Notiflix.Report.Info(
            '已经是最后一页了',
            ' ',
            '关闭'
        )
        return;
    }
    $("#pageNum").val(pageNum);
    listJob();
}

function listAttach() {
    var attachList = null;
    var token = localStorage.getItem("token");
    token = token.substring(1, token.length - 1);
    var user = JSON.parse(localStorage.getItem("userInfo"));
    $.ajax({
        type:"GET",
        async:false,              
        url:defaultUrl + "attach/listResumeAttach",
        headers:{"token":token},
        data:{"userId":user.userId},
        dataType:"json",
        crossDomain: true,
        success:function(data) {
            if (data.code == 200) {
                attachList = data;
                //setAttachList(data)
                //getSuccessMsg("发布成功");
            } else {
                //getInfoMsg(data.data);
            }
        },
        //error:error(),
    })
    return attachList;
}

function viewProfile(resumeId, attachId) {
    var url = null;
    if (attachId == null) {
        url = "candidates-profile.html?userId=" + resumeId;
    } else {
        var data = getResumeAttach(attachId);
        if (data.data == null) {
            getFailMsg("该附件已被投递者删除");
            return;
        }
        url = data.data.url;
    }
    window.open(url);
}

function updateDeliveryState(recordId, state) {
    Notiflix.Confirm.Show(
        '确认',
        '您确定要处理吗？',
        '确定',
        '取消',
        function(){ 
            var token = localStorage.getItem("token");
            token = token.substring(1, token.length - 1);
            var user = JSON.parse(localStorage.getItem("userInfo"));
            $.ajax({
                type:"POST",
                async:true,
                url:defaultUrl + "delivery/updateDeliveryState",
                headers:{"token":token},
                dataType:"json",
                data:{
                    "recordId":recordId,
                    "userId":user.userId,
                    "state":state
                },
                success:function(data) {
                    if (data.code == 200) {
                        getSuccessMsg("处理成功");
                    }
                    location.reload();
                }
            })
        },function(){ 
            // No button callbackalert('If you say so...');
        }
    );
    
}

function getResumeAttach(attachId) {
    var token = localStorage.getItem("token");
    token = token.substring(1, token.length - 1);
    var user = JSON.parse(localStorage.getItem("userInfo"));
    var attach = null;
    $.ajax({
        type:"GET",
        async:false,
        url:defaultUrl + "attach/getResumeAttach",
        headers:{"token":token},
        dataType:"json",
        data:{
            "attachId":attachId
        },
        success:function(data) {
            attach = data;
        }
    })
    return attach;
}

function getResume(userId) {
    var token = localStorage.getItem("token");
    token = token.substring(1, token.length - 1);
    var tmp = null;
    $.ajax({
        type:"GET",
        async:false,              
        url:defaultUrl + "resume/getResume",
        headers:{"token":token},
        data:{"userId":userId},
        dataType:"json",
        crossDomain: true,
        success:function(data) {
            if (data.code == 200) {
                console.log(data);
                tmp = data;
                //getSuccessMsg("发布成功");
            } else {
                getInfoMsg(data.data);
            }
        },
        //error:error(),
    })
    return tmp;
}

function setResumeEducation(data) {
    var educationList = data.data.resumeEducationList;
    console.log(educationList);
    for (var i = 0; i < educationList.length; i++) {
        if (i >= 1) {
            setDefaultSelect("#education-degree" + i, getEudcationCode(educationList[i].degree));
            $("#education-id" + i).val(educationList[i].id);
            $("#school" + i).val(educationList[i].school);
            $("#specialty" + i).val(educationList[i].specialty);
            $("#education-date-from" + i).val(educationList[i].dateFrom);
            $("#education-date-to" + i).val(educationList[i].dateTo);
        } else {
            setDefaultSelect("#education-degree", getEudcationCode(educationList[i].degree));
            $("#education-id").val(educationList[i].id);
            $("#school").val(educationList[i].school);
            $("#specialty").val(educationList[i].specialty);
            $("#education-date-from").val(educationList[i].dateFrom);
            $("#education-date-to").val(educationList[i].dateTo);
        }
        
    }
}

function setResumeWorkExperience(data) {
    var workExperienceList = data.data.resumeWorkExperienceList;
    for (var i = 0; i < workExperienceList.length; i++) {
        if (i >= 1) {
            $("#companyName" + i).val(workExperienceList[i].companyName);
            $("#work-date-from" + i).val(workExperienceList[i].dateFrom);
            $("#work-date-to" + i).val(workExperienceList[i].dateTo);
            $("#work-experience-id" + i).val(workExperienceList[i].id);
            $("#jobName" + i).val(workExperienceList[i].jobName);
            $("#city" + i).val(workExperienceList[i].city);
            $("#work-remark" + i).val(workExperienceList[i].remark);
        } else {
            $("#companyName").val(workExperienceList[i].companyName);
            $("#work-date-from").val(workExperienceList[i].dateFrom);
            $("#work-date-to").val(workExperienceList[i].dateTo);
            $("#work-experience-id").val(workExperienceList[i].id);
            $("#jobName").val(workExperienceList[i].jobName);
            $("#city").val(workExperienceList[i].city);
            $("#work-remark").val(workExperienceList[i].remark);
        }
        
    }
}

function setDefaultSelect(id, value) {
    var $select = $(id).selectize({
        create: true,
        dropdownParent: 'body'
    });
    var control = $select[0].selectize;
    control.addItem(value);
}

function setResume(data) {
    var resume = data.data.resume;
    $("#age").val(resume.age);
    $("#cityIntension").val(resume.cityIntension);
    
    if (resume.education != null) {
        setDefaultSelect("#resume-education", getEudcationCode(resume.education));
    }
    if (resume.workExperience != null) {
        setDefaultSelect("#resume-work", getWorkCode(resume.workExperience));
    }
    setDefaultSelect("#resume-maritalStatus", getMaritalCode(resume.maritalStatus));
    setDefaultSelect("#resume-gender", getGenderCode(resume.gender));
    $("#head-image").attr("src", resume.icon);
    $("#email").val(resume.email);
    //$("#gender").val(resume.gender);
    $("#icon").val(resume.icon);
    $("#jobIntension").val(resume.jobIntension);
    //$("#maritalStatus").val(resume.maritalStatus);
    $("#name").val(resume.name);
    $("#phone").val(resume.phone);
    $("#resumeId").val(resume.resumeId);
    $("#selfIntroduction").val(resume.selfIntroduction);
    $("#skill").val(resume.skill);
    $("#resume-id").val(resume.id);
}

function getScaleCode(scale) {
    if (scale == "0-20人") {
        return 1;
    } else if (scale == "20-99人") {
        return 2;
    } else if (scale == "100-499人") {
        return 3;
    } else if (scale == "500-999人") {
        return 4;
    } else if (scale == "1000-9999人") {
        return 5;
    } else if (scale == "10000人以上") {
        return 6;
    } else {
        return 0;
    }
}

function getScale(scale) {
    if (scale == 1) {
        return "0-20人";
    } else if (scale == 2) {
        return "20-99人";
    } else if (scale == 3) {
        return "100-499人";
    } else if (scale == 4) {
        return "500-999人";
    } else if (scale == 5) {
        return "1000-9999人";
    } else if (scale == 6) {
        return "10000人以上";
    } else {
        return "";
    }
}

function getStage(stage) {
    if (stage == 1) {
        return "未融资";
    } else if (stage == 2) {
        return "天使轮";
    } else if (stage == 3) {
        return "A轮";
    } else if (stage == 4) {
        return "B轮";
    } else if (stage == 5) {
        return "C轮";
    } else if (stage == 6) {
        return "D轮";
    } else if (stage == 7) {
        return "已上市";
    } else if (stage == 8) {
        return "不需要融资";
    } else {
        return "";
    }
}

function getStageCode(stage) {
    if (stage == "未融资") {
        return 1;
    } else if (stage == "天使轮") {
        return 2;
    } else if (stage == "A轮") {
        return 3;
    } else if (stage == "B轮") {
        return 4;
    } else if (stage == "C轮") {
        return 5;
    } else if (stage == "D轮") {
        return 6;
    } else if (stage == "已上市") {
        return 7;
    } else if (stage == "不需要融资") {
        return 8;
    } else {
        return 0;
    }
}

function getUserInfoById(userId) {
    var tmp = null;
    $.ajax({
        type:"GET",
        async:false,
        url:defaultUrl + "user/getUserInfoById",
        dataType:"json",
        data:{"userId":userId},
        success:function(data) {
            if (data.code == 200) {
                tmp = data.data.userEntity;
            }
        }
    })
    return tmp;
}

function updateUserInfo(userId) {
    var user = getUserInfoById(userId);
    console.log(user);
    localStorage.setItem("userInfo",JSON.stringify(user));
}

function getGenderCode(gender) {
    if (gender == "男") {
        return 1;
    } else {
        return 2;
    }
}

function getEudcationCode(education) {
    if (education == "初中及以下") {
        return 1;
    } else if (education == "中专/中技") {
        return 2;
    } else if (education == "高中") {
        return 3;
    } else if (education == "大专") {
        return 4;
    } else if (education == "本科") {
        return 5;
    } else if (education == "硕士") {
        return 6;
    } else if (education == "博士") {
        return 7;
    }
}

function getWorkCode(work) {
    if (work == "在校生") {
        return 1;
    } else if (work == "应届生") {
        return 2;
    } else if (work == "1年以内") {
        return 3;
    } else if (work == "1-3年") {
        return 4;
    } else if (work == "3-5年") {
        return 5;
    } else if (work == "5-10年") {
        return 6;
    } else if (work == "10年以上") {
        return 7;
    }
}

function getMaritalCode(maritalStatus) {
    if (maritalStatus == "未婚") {
        return 0;
    } else {
        return 1;
    }
}

function getStatusCode(status) {
    if (status == "开业") {
        return 1;
    } else {
        return 2;
    }
}

function getCount() {
    $.ajax({
            type:"GET",
            async:true,
            url:defaultUrl + "base/getCount",
            dataType:"json",
            success:function(data) {
                if (data.code == 200) {
                    $("#memberCount").html(data.data.memberCount);
                    $("#companyCount").html(data.data.companyCount);
                    $("#jobCount").html(data.data.jobCount);
                    $("#applicationCount").html(data.data.applicationCount);
                } else {
                    getInfoMsg(data.data);
                }
            },
            //error:error(),
    })
}