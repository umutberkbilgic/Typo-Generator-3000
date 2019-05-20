baho = () => {
  
  getLastMsg = () => {
    doc = document.getElementsByClassName("vW7d1");
    lastmsg = doc[doc.length - 1];
    return lastmsg.getElementsByClassName("selectable-text invisible-space copyable-text")[0].innerText;
  }

  sleep = (delay) => {
    var start = new Date().getTime();
    while (new Date().getTime() < start + delay);
  }

  simululateUserInput = () => new InputEvent('input', {bubbles: true});

  var textField = document.getElementsByClassName("_2S1VP copyable-text selectable-text")[0];
  document.getElementsByClassName("_39LWd")[0].setAttribute("style", "visibility: hidden");

  String.prototype.replaceAt=function(index, replacement) {
    return this.substr(0, index) + replacement+ this.substr(index + replacement.length);
  }  

  const failrate = 0.07;
  const randomrate = 0.15;

  const typos = {
    'a': "qwsz",    'b': "vghn",   'c': "xdfv",
    'd': "serfcx",  'e': "wsdfr",  'f': "dcvgtr",
    'g': "fvbhyt9", 'h': "gbnjuy", 'i': "ujko1",
    'j': "hnmkıu",  'k': "jmloi",  'l': "mkop",
    'm': "njkl",    'n': "bhjm",   'o': "iklp0",
    'p': "ol",      'q': "wa",     'r': "edft",
    's': "wazxde",  't': "rfgy",   'u': "yhji",
    'v': "cfgb",    'w': "qase",   'x': "zsdc",
    'y': "tghu",    'z': "asx",    'ı': "ujklo" , 
    'ğ':"pşiü",     'ü': "ğiş",    'ö': "mklç",
    'ç':"ölşi",     'ş':"çlp"};
  
  const randoms = ["ay", "of", "yha", "ya", "lan" , "wtf", "aq", "abi"];

  var lastMsg = getLastMsg().toLowerCase();

  for (var i = 0; i < lastMsg.length; i++) {
    var current = lastMsg.charAt(i);
    var decider = Math.random();
    var randomize = Math.random();
  
    if(current in typos){
      if (decider <= failrate){
        var typo = typos[current];
        const randomLetter = (typo).split('')[(Math.floor(Math.random() * typo.length ))];
        lastMsg = lastMsg.replaceAt(i, randomLetter); 
      }
    }
    else{
      if(randomize <= randomrate){
        var randomword = randoms[Math.floor(Math.random() * randoms.length)];
        lastMsg = lastMsg.replaceAt(i, " " + randomword + " ");
      }
    }
  }

  textField.innerHTML = lastMsg;
  textField.dispatchEvent(simululateUserInput());
  var sendButton = document.getElementsByClassName("_35EW6")[0];
  sendButton.click();
}