var attachJobId;
        var attachReceiver;

        function sendAttachRecord() {
            var attachId = $("input:radio[name=attachId]:checked").val();
            saveDeliveryRecord(attachJobId,attachId,attachReceiver);
        }

        function saveDeliveryRecord(jobId,attachId,receiver) {
            var token = localStorage.getItem("token");
            token = token.substring(1, token.length - 1);
            var user = JSON.parse(localStorage.getItem("userInfo"));
            var delivery = {
                "jobId":jobId,
                "attachId":attachId,
                "receiver":receiver,
                "sender":user.userId
            }
            $.ajax({
                type:"post",
                async:true,              
                url:defaultUrl + "delivery/saveDeliveryRecord",
                headers:{"token":token},
                data:JSON.stringify(delivery),
                contentType:"application/json;charset=utf-8",
                dataType:"json",
                crossDomain: true,
                success:function(data) {
                    if (data.code == 200) {
                        getSuccessMsg("投递成功");
                        
                    } else {
                        getFailMsg(data.data);
                    }
                },
                //error:error(),
            })
        }

        
        function apply(jobNo,receiver) {
            if (getUser() == null) {
                jump();
            }
            attachJobId = jobNo;
            attachReceiver = receiver;
            var token = localStorage.getItem("token");
            token = token.substring(1, token.length - 1);
            var user = JSON.parse(localStorage.getItem("userInfo"));
            Notiflix.Confirm.Show(
                '确认',
                '选择一项投递方式',
                '在线简历',
                '附件简历',
                function(){ 
                    saveDeliveryRecord(jobNo,null,receiver);
                },function(){ 
                    
                    var data = listAttach();
                    var attachList = data.data;
                    setAttachRadio(attachList)
                    $("#modal-btn").click();
                }
            );
        }

        function setAttachRadio(attachList) {
            $("#attach-list").empty();
            for (var i = 0; i < attachList.length; i++) {
                $("#attach-list").append('<div class="custom-control custom-radio"><input type="radio" id="customRadio29'+i+'" name="attachId" class="custom-control-input" value="'+attachList[i].attachId+'">'+
                                            '<label class="custom-control-label ml-1 text-muted" for="customRadio29'+i+'">'+attachList[i].fileName+'</label></div>')
            }
        }