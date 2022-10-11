async function typeSentence(sentence, eleRef, delay = 60) {
  const letters = sentence.split("");
  let i = 0;
  while(i < letters.length) {
    await waitForMs(delay);
    $(eleRef).append(letters[i]);
    i++
  }
  return;
}


function waitForMs(ms) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

typeSentence("Welcome, human! How can I help today?", "#sentence")


$("#provider").change(function(){
    $("#provider option:selected").each(function() {
        for(let elem of $(".provider-section")){
            if($(this).text() == $(elem).attr("id")){
                $(elem).show();
                $(elem).children().prop("disabled", false);
            } else {
                $(elem).hide();
                $(elem).children().prop("disabled", true);
            }
        }
    });
});


