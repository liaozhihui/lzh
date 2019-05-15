/**
 * Created by csdn on 19-4-12.
 */

function createXhr() {
    var xhr=null
    if (window.XMLHttpRequest){
        xhr=new XMLHttpRequest()
    }else{
        xhr=new ActiveXObject('Microsoft.XMLHttp')
    }

    return xhr
}
