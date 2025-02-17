document.addEventListener("DOMContentLoaded", function () {
  // Flatpicker Initialize for appointment_date field
  flatpickr("#id_appointment_date", {
    enableTime: true,
    dateFormat: "Y-m-d H:i", // Date and time format
    defaultHour: 12, // Default time (optional)
    defaultMinute: 0, // Default minutes (optional)
    minuteIncrement: 5, // Allow incrementing by 5 minutes
    time_24hr: true, // Use 24-hour format
    minDate: "today"  // Prevent selecting a past date
  });

  // Function to filter Doctors based on Specialisation and Location
  // Function triggered by CreateAppointmentForm user input for Specialisation and Location
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

          // Default option
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
              option.value = doctor.id; // Set doctor id as value
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

  // Delete Appointment Popup Validation
  // Function to handle the delete confirmation
  function confirmDeleteHandler(event) {
    // Prevent the default action of the link (which is to go to a URL)
    event.preventDefault();

    // Get the appointment ID from the clicked button
    const appointmentId = event.target.getAttribute("data-appointment-id");

    // Open the modal and pass the appointmentId to the modal
    openDeleteModal(appointmentId);
  }

  // Function to open the delete modal / Internet Solution, currently not working
  function openDeleteModal(appointmentId) {
    $("#deleteModal").modal("show"); // Show the modal

    // Store the appointment ID in the modal's delete button
    $("#confirmDelete").attr("data-appointment-id", appointmentId);
  }

  // When the "Delete" button inside the modal is clicked
  $("#confirmDelete").click(function () {
    const appointmentId = $(this).attr("data-appointment-id"); // Get the appointment ID

    // Make the AJAX request to delete the appointment
    $.ajax({
      url: "/appointments/delete/" + appointmentId + "/", // Adjust URL for your delete endpoint
      type: "POST",
      data: {
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(), // Ensure CSRF protection
      },
      success: function (response) {
        // On success, hide the modal and reload the page or handle the response
        $("#deleteModal").modal("hide");
        location.reload(); // Optionally reload to reflect the changes
      },
      error: function (xhr, errmsg, err) {
        console.error("Error deleting appointment: ", errmsg);
      },
    });
  });
});
