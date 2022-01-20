

var images = [];
function init() {
  d3.json("https://nasa-day-picture.herokuapp.com/data").then(function(data, error)   {
  // d3.json("http://127.0.0.1:5000/data").then(function(data, error)   {
    
    // console.log("data=",data);
    // console.log("data=",data.result[0]);
  
    size = data.result.length - 1;
    // console.log(size);

    
    for (i = 0; i < size; i++){
          images [i] = data.result[i];
          
          d3.select("tbody")
            .selectAll("tr")
            .data(images)
            .enter()
            .append("tr")
            .html(function(d) {
              
              return `<td>${d.date}</td><td><a href="${d.url}"><img src="${d.url}" class="col-md-24  img-thumbnail"> </a></td><td>${d.explanation}</td><td></td>`;
             
            });

        
    }
   

  }).catch(function(error) {
  console.log(error);
  });
}


init();
