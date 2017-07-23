/* Google Analytics Tracking Code */
function runAnalytics() {
    var trackingCode = 'UA-XXXXXX';
    var gaTrackingCode = "(function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;e=o.createElement(i);r=o.getElementsByTagName(i)[0];e.src='https://www.google-analytics.com/analytics.js';r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));ga('create','" + trackingCode + "','auto');ga('send','pageview');";
    document.getElementById('google-analytics-tracking').innerHTML = gaTrackingCode;
}
