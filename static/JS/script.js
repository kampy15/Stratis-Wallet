function straxFun(){
    alert("Now you will be redirected to a Third-party website to buy strax where you have to login/register again into their respective system,"+"            "+"Press OK to continue.")
    window.open("https://www.binance.com/en-IN/trade/STRAX_USDT", "_blank");
}

function copyFun(){
    var address=document.getElementById('add').innerHTML;
    navigator.clipboard.writeText(address);
    alert("Your " +address+" is copied to your clipboard.");

}


var qr;
(function() {
        qr = new QRious({
        element: document.getElementById('qr-code'),
        size: 200,
        value: ''
    });
})();

function generateQRCode() {
    var qrtext = document.getElementById('add').innerHTML;
    document.getElementById("qr-result").innerHTML = "QR code for " + qrtext +":";
    // alert(qrtext);
    qr.set({
        foreground: 'black',
        size: 200,
        value: qrtext
    });
}