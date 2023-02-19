$(function(){
    let socket = new WebSocket('ws://46.146.220.216:4242/ws')
    socket.onopen = function (e) {
        console.log('ку')
        console.log(e)
    }
    socket.onerror = function(error) {
        console.log('неку')
        console.log(error)
    }
    socket.onmessage = function (event) {
        let obj = JSON.parse(event.data)
        console.log(obj)
        let temp=-1
        $('#date_update').html('Дата обновления - '+obj.refresh_data)
        for(let i=1;i<=3;i++){
            for(let j=1;j<=2;j++){
                temp++
                $('.css_name_ek').eq(temp).html(obj.sinter_machines[i].exhausters[j].name)
                $('.css_rot_name').eq(temp).html(obj.sinter_machines[i].exhausters[j].rotor_name)
                let date=new Date(obj.sinter_machines[i].exhausters[j].last_change*1000)
                let year=date.getFullYear()
                let month = (date.getMonth() + 1).toString().padStart(2, '0'); // "04"
                let day = date.getDate().toString().padStart(2, '0');
                $('.css_rot_date').eq(temp).html(day+'.'+month+'.'+year)
                $('.css_sutki_kogda').eq(temp).html(Math.round((Math.floor(Date.now()/1000)-obj.sinter_machines[i].exhausters[j].last_change)/60/60/24)+' сут')
                $('.css_sutki_prognoz_val').eq(temp).html(Math.round((Math.floor(Date.now()/1000)-obj.sinter_machines[i].exhausters[j].prediction)/60/60/24)+' сут')
                let str_p=''
                let lf=''
                let pr=''
                obj.sinter_machines[i].exhausters[j].sensors.forEach(function(el,index){
                    lf=''
                    pr=''
                    if(el.signals.temp!=undefined){
                        lf=get_T(el.signals.temp)
                        if(el.signals.vibr==undefined){
                            lf=''
                            pr=get_T(el.signals.temp)
                        }
                        
                    }
                    if(el.signals.vibr!=undefined){
                        pr=get_V(el.signals.vibr)
                    }
                    if(el.signals.oil_level!=undefined){
                        pr=get_L(el.signals.oil_level)
                    }
                    str_p+='<div class="css_pod_div" id_e="'+(temp)+'" id_p="'+index+'" style="margin-bottom:5px;">'+
                    '<div class="css_cell1">'+
                        '<div class="css_pod_text">'+
                         el.title+
                        '</div>'+
                    '</div>'+
                    '<div class="css_cell2">'+
                        '<div class="css_cell_d1">'+
                          lf+
                        '</div>'+
                        '<div class="css_cell_d2">'+
                          pr+
                        '</div>'+
                    '</div>'+
                '</div>'
                })
                
            $('.all_pod').eq(temp).html(str_p)
                    lf=''
                    pr=''
                    str_p=''
                    obj.sinter_machines[i].exhausters[j].warnings.forEach(function(el,index){
                        lf=''
                        pr=''
                        if(el.signals.temp!=undefined){
                            lf=get_T(el.signals.temp)
                            if(el.signals.vibr==undefined){
                                lf=''
                                pr=get_T(el.signals.temp)
                            }
                            
                        }
                        if(el.signals.vibr!=undefined){
                            pr=get_V(el.signals.vibr)
                        }
                        if(el.signals.oil_level!=undefined){
                            pr=get_L(el.signals.oil_level)
                        }
                        str_p+='<div class="css_pod_div" id_e="'+(temp)+'" id_p="'+index+'" style="margin-bottom:5px;">'+
                        '<div class="css_cell1">'+
                            '<div class="css_pod_text">'+
                             el.title+
                            '</div>'+
                        '</div>'+
                        '<div class="css_cell2">'+
                            '<div class="css_cell_d1">'+
                              lf+
                            '</div>'+
                            '<div class="css_cell_d2">'+
                              pr+
                            '</div>'+
                        '</div>'+
                    '</div>'
                    })        
            $('.all_pred').eq(temp).html(str_p)

            $('.css_pod_div').hover(function () {
                $('[beg="'+(parseInt($(this).attr('id_p'))+1)).eq($(this).attr('id_e')).attr('fill','blue')
                
                
                
            }, function () {
                $('[beg="'+(parseInt($(this).attr('id_p'))+1)).eq($(this).attr('id_e')).attr('fill','#414F4F')
                
            })

            


            }
            
        }
       console.log( obj.sinter_machines[1].exhausters[1].name)
    }
    $('#svg_p4').hover(function () {
        console.log('завелось')
    }, function () {
        console.log('уборалось')
    })
    
    $('.click_all_pod').on('click',function(){
        if($(this).attr('src')=='btn.png'){
            $(this).attr('src','btn2.png')
            $(this).parent().next().css('display','none')
        }else{
            $(this).attr('src','btn.png')
            $(this).parent().next().css('display','')
        }
    })
    
    $('.click_all_pred').on('click',function(){
        if($(this).attr('src')=='btn.png'){
            $(this).attr('src','btn2.png')
            $(this).parent().next().css('display','none')
        }else{
            $(this).attr('src','btn.png')
            $(this).parent().next().css('display','')
        }
    })
    function get_L(number) {
    
        let b_color = '#F4F4F4'
        let color = '#868686'
        if (parseInt(number) == 1) {
            b_color = '#FEF1DB'
            color = '#F37E0D'
    
        }
        if (parseInt(number) == 2) {
            b_color = '#FCDBCB'
            color = '#E32112'
        }
        return '<svg width="36" height="21" viewBox="0 0 36 21" fill="none" xmlns="http://www.w3.org/2000/svg">'+
        '<rect x="1.49677" y="1.02316" width="34.0035" height="19.0035" rx="1.5" fill="'+b_color+'"/>'+
        '<path d="M8.16777 5.9249V13.6079C8.16777 13.7552 8.15477 13.8592 8.12877 13.9199L8.15477 13.9459C8.21543 13.9199 8.32377 13.9069 8.47977 13.9069H12.2238V15.0249H6.99777V5.9249H8.16777Z" fill="black"/>'+
        '<path d="M27.4991 12.5252C27.4991 15.2873 25.7602 17.0262 22.9981 17.0262C20.2359 17.0262 18.4971 15.2873 18.4971 12.5252C18.4971 9.5611 21.7237 5.55961 22.7133 4.40217C22.7485 4.36104 22.7922 4.32803 22.8414 4.3054C22.8906 4.28276 22.9441 4.27104 22.9982 4.27104C23.0524 4.27104 23.1059 4.28276 23.1551 4.3054C23.2042 4.32803 23.2479 4.36104 23.2831 4.40217C24.2724 5.55961 27.4991 9.5611 27.4991 12.5252Z" stroke="'+color+'" stroke-width="1.00189" stroke-miterlimit="10"/>'+
        '<path d="M25.7504 12.7747C25.7504 13.372 25.5131 13.9449 25.0907 14.3672C24.6684 14.7896 24.0955 15.0269 23.4982 15.0269" stroke="'+color+'" stroke-width="1.00189" stroke-linecap="round" stroke-linejoin="round"/>'+
        '<rect x="1.49677" y="1.02316" width="34.0035" height="19.0035" rx="1.5" stroke="'+color+'"/>'+
        '</svg>'
    
    }
    function get_V(number) {
    
        let b_color = '#F4F4F4'
        let color = '#868686'
        if (parseInt(number) == 1) {
            b_color = '#FEF1DB'
            color = '#F37E0D'
    
        }
        if (parseInt(number) == 2) {
            b_color = '#FCDBCB'
            color = '#E32112'
        }
        return '<svg width="38" height="21" viewBox="0 0 38 21" fill="none" xmlns="http://www.w3.org/2000/svg">'+
                '<rect x="1.49677" y="1.02316" width="36.0035" height="19.0035" rx="1.5" fill="'+b_color+'"/>'+
                '<path d="M14.1478 5.9249L10.1568 15.1549H10.0268L6.02277 5.9249H7.40077L9.61077 11.3719C9.80143 11.8486 9.9531 12.3989 10.0658 13.0229H10.1178C10.2044 12.4596 10.3561 11.9092 10.5728 11.3719L12.7828 5.9249H14.1478Z" fill="black"/>'+
                '<path d="M23.5068 8.5322C23.0188 9.08147 22.7493 9.79068 22.7493 10.5254C22.7493 11.2601 23.0188 11.9694 23.5068 12.5186" stroke="'+color+'" stroke-width="1.00189" stroke-linecap="round" stroke-linejoin="round"/>'+
                '<path d="M26.5246 12.5186C27.0126 11.9694 27.2822 11.2601 27.2822 10.5254C27.2822 9.79068 27.0126 9.08147 26.5246 8.5322" stroke="'+color+'" stroke-width="1.00189" stroke-linecap="round" stroke-linejoin="round"/>'+
                '<path d="M21.9133 6.93918C21.0041 7.91184 20.4984 9.19355 20.4984 10.525C20.4984 11.8564 21.0041 13.1381 21.9133 14.1107" stroke="'+color+'" stroke-width="1.00189" stroke-linecap="round" stroke-linejoin="round"/>'+
                '<path d="M28.1167 14.1107C29.0258 13.1381 29.5316 11.8564 29.5316 10.525C29.5316 9.19355 29.0258 7.91184 28.1167 6.93918" stroke="'+color+'" stroke-width="1.00189" stroke-linecap="round" stroke-linejoin="round"/>'+
                '<path d="M29.8757 15.5253C31.1037 14.1489 31.7823 12.3688 31.7823 10.5243C31.7823 8.67968 31.1037 6.89958 29.8757 5.52316" stroke="'+color+'" stroke-width="1.00189" stroke-linecap="round" stroke-linejoin="round"/>'+
                '<path d="M20.1545 5.52316C18.9266 6.89958 18.2479 8.67968 18.2479 10.5243C18.2479 12.3688 18.9266 14.1489 20.1545 15.5253" stroke="'+color+'" stroke-width="1.00189" stroke-linecap="round" stroke-linejoin="round"/>'+
                '<rect x="1.49677" y="1.02316" width="36.0035" height="19.0035" rx="1.5" stroke="'+color+'"/>'+
                '</svg>'
    
        }
    function get_T(number) {
    
        let b_color = '#F4F4F4'
        let color = '#868686'
        if (parseInt(number) == 1) {
            b_color = '#FEF1DB'
            color = '#F37E0D'
    
        }
        if (parseInt(number) == 2) {
            b_color = '#FCDBCB'
            color = '#E32112'
        }
        return '<svg width="38" height="21" viewBox="0 0 38 21" fill="none" xmlns="http://www.w3.org/2000/svg">' +
            '<rect x = "1.49677" y = "1.02316" width = "36" height = "19" rx = "1.5" fill="' + b_color + '" />' +
            '<path d="M13.5878 5.92316V7.04116H11.2608C11.0961 7.04116 10.9834 7.02816 10.9228 7.00216L10.9098 7.02816C10.9358 7.08883 10.9488 7.19283 10.9488 7.34016V15.0232H9.77877V7.34016C9.77877 7.19283 9.79177 7.08883 9.81777 7.02816L9.79177 7.00216C9.7311 7.02816 9.62277 7.04116 9.46677 7.04116H7.12677V5.92316H13.5878Z" fill="black"/>' +
            '<g clip-path="url(#clip0_392_14640)">' +
            '<path d="M25.6127 11.9703C25.5771 11.9478 25.5478 11.9166 25.5275 11.8797C25.5072 11.8429 25.4965 11.8015 25.4965 11.7594V5.02435C25.4965 4.62653 25.3384 4.245 25.0571 3.96369C24.7758 3.68239 24.3943 3.52435 23.9965 3.52435C23.5986 3.52435 23.2171 3.68239 22.9358 3.96369C22.6545 4.245 22.4965 4.62653 22.4965 5.02435V11.7594C22.4964 11.8014 22.4857 11.8427 22.4655 11.8795C22.4452 11.9163 22.416 11.9474 22.3805 11.97C21.9362 12.2594 21.5751 12.6598 21.3329 13.1315C21.0907 13.6032 20.9758 14.1299 20.9996 14.6597C21.0353 15.4425 21.376 16.1803 21.9487 16.7152C22.5214 17.2501 23.2807 17.5397 24.0641 17.522C24.8476 17.5043 25.593 17.1808 26.141 16.6206C26.689 16.0604 26.996 15.308 26.9965 14.5244C26.9967 14.0171 26.8702 13.5178 26.6286 13.0718C26.3869 12.6258 26.0377 12.2472 25.6127 11.9703V11.9703Z" stroke="' + color + '" stroke-width="1.00189" stroke-miterlimit="10" stroke-linecap="round"/>' +
            '<path d="M23.9964 6.02475V14.5248" stroke="' + color + '" stroke-width="1.00189" stroke-miterlimit="10" stroke-linecap="round"/>' +
            '<path d="M23.9973 16.0254C24.8264 16.0254 25.4984 15.3534 25.4984 14.5243C25.4984 13.6953 24.8264 13.0232 23.9973 13.0232C23.1683 13.0232 22.4962 13.6953 22.4962 14.5243C22.4962 15.3534 23.1683 16.0254 23.9973 16.0254Z" fill="' + color + '"/>' +
            '</g>' +
            '<rect x="1.49677" y="1.02316" width="36" height="19" rx="1.5" stroke="' + color + '"/>' +
            '<defs>' +
            '<clipPath id="clip0_392_14640">' +
            '<rect width="16" height="16" fill="white" transform="translate(15.9968 2.52316)"/>' +
            '</clipPath>' +
            '</defs>' +
            '</svg>'
    }
    
})
