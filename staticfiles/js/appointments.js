document.addEventListener("DOMContentLoaded", function () {
    const deleteButtons = document.querySelectorAll(".btn-delete-appointment");
    const deleteForm = document.getElementById("deleteForm");
  
    deleteButtons.forEach(button => {
      button.addEventListener("click", function () {
        const appointmentId = this.getAttribute("data-appointment_id");
        const baseUrl = this.getAttribute("data-delete-url").replace(/0\/?$/, "");
        deleteForm.action = `${baseUrl}${appointmentId}/`;
      });
    });
  });