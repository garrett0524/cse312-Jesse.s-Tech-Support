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
  var formData = new FormData();
  var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  formData.append('profile_picture', file);
  // Send the file to the backend with AJAX
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/upload_profile_picture/', true); // Update the URL to the backend endpoint
  xhr.setRequestHeader("X-CSRFToken", csrftoken);
  xhr.send(formData);
}

// Function to save the user's bio
function saveBio() {
  var bio = document.getElementById('bio').value;
  // Send the bio to the backend with AJAX
  var xhr = new XMLHttpRequest();
  var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  xhr.open('POST', '/profile/', true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.setRequestHeader('X-CSRFToken', csrftoken);
  xhr.onload = function() {
      if (xhr.status === 200) {
          console.log('Bio saved successfully');
      }
  };
  xhr.send('bio=' + encodeURIComponent(bio));
}