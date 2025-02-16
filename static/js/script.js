// Ensure Script runs after the DOM is fully loaded but before DOM manipulations
document.addEventListener("DOMContentLoaded", function () {
  // Function to filter Doctors based on Specialisation and Location
  // Function triggered by CreateAppointmentForm user input
  function updateDoctors() {
    var specialisation = document.getElementById(
      "id_doctor_specialisation"
    ).value;
    var location = document.getElementById("id_doctor_location").value;

    // Only proceed if both specialisation and location are selected
    if (specialisation && location) {
      fetch(
        `/get-doctors/?specialisation=${specialisation}&location=${location}`
      )
        .then((response) => response.json())
        .then((data) => {
          var doctorSelect = document.getElementById("id_doctor");
          doctorSelect.innerHTML = ""; // Clear existing options
          var defaultOption = document.createElement("option");
          defaultOption.text = "Select Doctor";
          doctorSelect.appendChild(defaultOption);

          // If no doctors are available, show a message
          if (data.doctors.length === 0) {
            document.getElementById("no-doctor-message").style.display =
              "block"; // Show message
            doctorSelect.disabled = true; // Disable the dropdown
          } else {
            document.getElementById("no-doctor-message").style.display = "none"; // Hide message
            doctorSelect.disabled = false; // Enable the dropdown

            // Dynamically populate the Doctor option
            data.doctors.forEach((doctor) => {
              var option = document.createElement("option");
              option.value = doctor.id;
              option.text = doctor.full_name;
              doctorSelect.appendChild(option);
            });
          }
        });
    }
  }

  // Attach Event Listeners to the fields Specialisation and Location
  document
    .getElementById("id_doctor_specialisation")
    .addEventListener("change", updateDoctors);
  document
    .getElementById("id_doctor_location")
    .addEventListener("change", updateDoctors);
});
