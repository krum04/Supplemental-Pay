// timeCalc.js
 // get all the input elements
	const inputs = document.querySelectorAll('input[type="time"]');
	//  attach onchange event listeners to all the input elements
	inputs.forEach(input => input.addEventListener('change', calculateTotalHours));
    // run function on load
    window.addEventListener('load', function() {
        // your code here
        calculateTotalHours(); // call the function you want to run on page load
      });
	// function to calculate the total hours
    function calculateTotalHours() {
        let totalMinutes = 0;
      
        // iterate over all the input elements and calculate the total hours
        inputs.forEach(input => {
          // get the day and time value of the input element
          const day = input.parentNode.parentNode.children[0].textContent.toLowerCase();
          const startTime = input.parentNode.parentNode.children[1].children[0].value;
          const finishTime = input.parentNode.parentNode.children[2].children[0].value;
      
          // calculate the hours and minutes from the start time
          const startHours = parseInt(startTime.substring(0, 2));
          const startMinutes = parseInt(startTime.substring(3));
      
          // calculate the hours and minutes from the finish time
          const finishHours = parseInt(finishTime.substring(0, 2));
          const finishMinutes = parseInt(finishTime.substring(3));
      
          // calculate the total minutes for the day
          let dayMinutes = ((finishHours - startHours) * 60) + (finishMinutes - startMinutes);
      
          // if dayMinutes is NaN or negative, set it to zero
          if (isNaN(dayMinutes) || dayMinutes < 0) {
            dayMinutes = 0;
          }
      
          // set the total hours for the day
          document.getElementById(`${day}-total`).value = `${Math.floor(dayMinutes / 60)}:${(dayMinutes % 60).toString().padStart(2, '0')}`;
        
          // add the day minutes to the total minutes
          totalMinutes += dayMinutes;
          
        });
        
        // calculate the total hours and minutes
        totalMinutes /= 2;
        const totalHours = Math.floor(totalMinutes / 60);
        const totalMinutesRemainder = totalMinutes % 60;
      
        // set the total hours for the week
        document.getElementById('total-hours').value = `${totalHours}:${totalMinutesRemainder.toString().padStart(2, '0')}`;
      }
      
      
