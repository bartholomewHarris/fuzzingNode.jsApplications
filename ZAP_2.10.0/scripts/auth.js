// Logging with the script name is super helpful!
function logger() {
  print('[' + this['zap.script.name'] + '] ' + arguments[0]);
}

// Control.getSingleton().getExtensionLoader().getExtension(ExtensionUserManagement.class);
var HttpSender    = Java.type('org.parosproxy.paros.network.HttpSender');
var ScriptVars    = Java.type('org.zaproxy.zap.extension.script.ScriptVars');
var HtmlParameter = Java.type('org.parosproxy.paros.network.HtmlParameter')
var COOKIE_TYPE   = org.parosproxy.paros.network.HtmlParameter.Type.cookie;

function sendingRequest(msg, initiator, helper) {  
  if (initiator === HttpSender.AUTHENTICATION_INITIATOR) {
    logger("Trying to auth")
  return msg;
  }

  var token = ScriptVars.getGlobalVar("jwt-token")
  // var token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwidXNlcm5hbWUiOiIiLCJlbWFpbCI6ImFkbWluQGp1aWNlLXNoLm9wIiwicGFzc3dvcmQiOiIwMTkyMDIzYTdiYmQ3MzI1MDUxNmYwNjlkZjE4YjUwMCIsInJvbGUiOiJhZG1pbiIsImRlbHV4ZVRva2VuIjoiIiwibGFzdExvZ2luSXAiOiIwLjAuMC4wIiwicHJvZmlsZUltYWdlIjoiYXNzZXRzL3B1YmxpYy9pbWFnZXMvdXBsb2Fkcy9kZWZhdWx0QWRtaW4ucG5nIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDIxLTA0LTIxIDAzOjMwOjI2LjYwNSArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDIxLTA0LTIxIDAzOjMwOjI2LjYwNSArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE2MTg5NzYzNDAsImV4cCI6MTYxODk5NDM0MH0.FLcEE2qDKJF0z0v241WNPNc-j7H_fywK-00sg7Q4vobqcFw-EcmJKkjFF_IoHITgMVhZE_Yi2yVOKgQvzmXB1OZxzkzJtAZ3u0-G5-FCDAzLxqDhgcyxI-LMGc1_oQaGrTPGL3mnKodxC5t_Gts7HIKafGgWJpo2dB8ukgj1Yys"
  if (!token) {return;}
  var headers = msg.getRequestHeader();
  var cookie = new HtmlParameter(COOKIE_TYPE, "token", token);
  msg.getRequestHeader().getCookieParams().add(cookie);
  // For all non-authentication requests we want to include the authorization header
  logger("Added authorization token " + token.slice(0, 20) + " ... ")
  msg.getRequestHeader().setHeader('Authorization', 'Bearer ' + token);
  return msg;
}

function responseReceived(msg, initiator, helper) {
  var resbody     = msg.getResponseBody().toString()
  var resheaders  = msg.getResponseHeader()

  if (initiator !== HttpSender.AUTHENTICATION_INITIATOR) {
     var token = ScriptVars.getGlobalVar("jwt-token");
    // var token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MSwidXNlcm5hbWUiOiIiLCJlbWFpbCI6ImFkbWluQGp1aWNlLXNoLm9wIiwicGFzc3dvcmQiOiIwMTkyMDIzYTdiYmQ3MzI1MDUxNmYwNjlkZjE4YjUwMCIsInJvbGUiOiJhZG1pbiIsImRlbHV4ZVRva2VuIjoiIiwibGFzdExvZ2luSXAiOiIwLjAuMC4wIiwicHJvZmlsZUltYWdlIjoiYXNzZXRzL3B1YmxpYy9pbWFnZXMvdXBsb2Fkcy9kZWZhdWx0QWRtaW4ucG5nIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDIxLTA0LTIxIDAzOjMwOjI2LjYwNSArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDIxLTA0LTIxIDAzOjMwOjI2LjYwNSArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE2MTg5NzYzNDAsImV4cCI6MTYxODk5NDM0MH0.FLcEE2qDKJF0z0v241WNPNc-j7H_fywK-00sg7Q4vobqcFw-EcmJKkjFF_IoHITgMVhZE_Yi2yVOKgQvzmXB1OZxzkzJtAZ3u0-G5-FCDAzLxqDhgcyxI-LMGc1_oQaGrTPGL3mnKodxC5t_Gts7HIKafGgWJpo2dB8ukgj1Yys"
     if (!token) {return;}

     var headers = msg.getRequestHeader();
     var cookies = headers.getCookieParams();
     var cookie = new HtmlParameter(COOKIE_TYPE, "token", token);
       
     if (cookies.contains(cookie)) {return;}
     msg.getResponseHeader().setHeader('Set-Cookie', 'token=' + token + '; Path=/;');
     return;
  }

  logger("Handling auth response")
  if (resheaders.getStatusCode() > 299) {
    logger("Auth failed")
    return;
  } 

  // Is response JSON? @todo check content-type
  if (resbody[0] !== '{') {return;}
  try {
    var data = JSON.parse(resbody);
  } catch (e) {
    return;
  }
  
  // If auth request was not succesful move on
  if (!data['authentication']) {return;}
  
  // @todo abstract away to be configureable
  var token = data["authentication"]["token"]
  logger("Capturing token for JWT\n" + token)
  ScriptVars.setGlobalVar("jwt-token", token)
  msg.getResponseHeader().setHeader('Set-Cookie', 'token=' + token + '; Path=/;');
}