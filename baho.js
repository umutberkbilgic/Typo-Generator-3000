baho = (customString, customFailRate, customRandomRate) => {
  
  // retrieves last message in the current whatsapp web chat window
  getLastMsg = () => {
    doc = document.getElementsByClassName("vW7d1");
    lastmsg = doc[doc.length - 1];
    return lastmsg.getElementsByClassName("selectable-text invisible-space copyable-text")[0].innerText;
  }

  // generate random integer between 0,max
  randomInRange = (max) => {
    return Math.floor(Math.random() * max + 1);
  }

  // simulate an input event to make the send button appear
  simululateUserInput = () => {
    return new InputEvent('input', {bubbles: true});
  }

  // provide replace function for strings
  String.prototype.replaceAt = function(index, replacement){
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
  }  

  // constants
  const textFieldClassName = "_2S1VP copyable-text selectable-text";
  const textFieldParentClassName = "_39LWd";
  const sendButtonClassName = "_35EW6"; 

  const failRate = customFailRate ? customFailRate : 0.07;
  const randomRate = customRandomRate ? customRandomRate : 0.15;

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
  
  const randoms = ["ay", "of", "yha", "ya", "lan" , "wtf", "aq", "abi", "yeter", "amk"];

  // if customString is given; use it
  var lastMsg = customString ? customString : getLastMsg();

  // get DOM for textfield and set its parents visibility to hidden
  var textField = document.getElementsByClassName( textFieldClassName )[0];
  document.getElementsByClassName( textFieldParentClassName )[0].setAttribute("style", "visibility: hidden");

  // for each character in string
  for (var i = 0; i < lastMsg.length; i++) {
    var current = lastMsg.charAt(i).toLowerCase();
    var typoDecider = Math.random();
    var randomDecider = Math.random();
  
    if(current in typos){
      if (typoDecider <= failRate){
        // there is typo now
        var typo = typos[current];
        const randomLetter = (typo).split('')[ randomInRange(typo.length) ];
        lastMsg = lastMsg.replaceAt(i, randomLetter); 
      }
    }
    else{
      if(randomDecider <= randomRate){
        // there is random now
        var randomWord = randoms[ randomInRange(randoms.length) ];
        lastMsg = lastMsg.replaceAt(i, " " + randomWord + " ");
      }
    }
  }

  // set text field to bahadirized message and dispatch input
  textField.innerHTML = lastMsg;
  textField.dispatchEvent(simululateUserInput());

  // find the send button and click it
  var sendButton = document.getElementsByClassName( sendButtonClassName )[0];
  sendButton.click();
}