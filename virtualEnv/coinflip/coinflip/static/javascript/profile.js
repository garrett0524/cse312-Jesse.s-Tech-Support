
document.getElementById('pictureUpload').addEventListener('change', function(e) {
    var file = e.target.files[0];
    
    var reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('profilePicture').src = e.target.result;
        uploadProfilePicture(file); // call upload pro pic function

    };
    reader.readAsDataURL(file);
});

// Function to handle uploading the profile picture to the backend
function uploadProfilePicture(file) {
    var maxSize = 2 * 1024 * 1024; // 2 MB in bytes

    if (file.size > maxSize) {
        alert("File size exceeds the limit of 2 MB. Please choose a smaller file.");
        return;
    }

    var formData = new FormData();
    var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    formData.append('profile_picture', file);

    // Send the file to the backend with AJAX
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload_profile_picture/', true);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(formData);
}
  
  function editProfile() {
    var bio = prompt("Enter your bio:", "{{ user.bio }}");
    if (bio !== null) {
      document.getElementById('bio').textContent = bio;
      // Update the bio in the backend (e.g., using AJAX or submitting a form)
    }
  }