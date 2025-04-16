document.addEventListener("DOMContentLoaded", function () {
  try {
    // Try to get the form elements
    const specField = document.getElementById("id_doctor_specialisation");
    const locField = document.getElementById("id_doctor_location");
    const doctorSelect = document.getElementById("id_doctor");

    // If any of the elements are missing, throw an error
    if (!specField || !locField || !doctorSelect) {
      throw new Error("One or more form elements are missing!");
    }

    // Initialize the Flatpickr for the appointment date field
    flatpickr("#id_appointment_date", {
      enableTime: true,
      dateFormat: "Y-m-d H:i", // Date and time format
      defaultHour: 12, // Default time (optional)
      defaultMinute: 0, // Default minutes (optional)
      minuteIncrement: 5, // Allow incrementing by 5 minutes
      time_24hr: true, // Use 24-hour format
      minDate: "today"  // Prevent selecting a past date
    });

    // Function to update the doctor dropdown based on the selected specialisation and location
    function updateDoctors() {
      var specialisation = specField.value;
      var location = locField.value;

      // Only proceed if both specialisation and location are selected
      if (specialisation && location) {
        fetch(`/get-doctors/?specialisation=${specialisation}&location=${location}`)
          .then((response) => response.json())
          .then((data) => {
            doctorSelect.innerHTML = ""; // Clear existing options

            // Default option
            var defaultOption = document.createElement("option");
            defaultOption.text = "Select Doctor";
            doctorSelect.appendChild(defaultOption);

            // If no doctors are available, show a message
            if (data.doctors.length === 0) {
              document.getElementById("no-doctor-message").style.display = "block"; // Show message
              doctorSelect.disabled = true; // Disable the dropdown
            } else {
              document.getElementById("no-doctor-message").style.display = "none"; // Hide message
              doctorSelect.disabled = false; // Enable the dropdown

              // Dynamically populate the Doctor option
              data.doctors.forEach((doctor) => {
                var option = document.createElement("option");
                option.value = doctor.id; // Set doctor id as value
                option.text = doctor.full_name;
                doctorSelect.appendChild(option);
              });
            }
          });
      }
    }

    // Attach event listeners to the Specialisation and Location fields
    specField.addEventListener("change", updateDoctors);
    locField.addEventListener("change", updateDoctors);

  } catch (e) {
    // Log any errors (such as missing form elements) to the console
    console.error(e.message);
  }
});