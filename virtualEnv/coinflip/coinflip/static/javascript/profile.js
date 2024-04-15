document.getElementById('pictureUpload').addEventListener('change', function(e) {
    var file = e.target.files[0];
    var reader = new FileReader();
    reader.onload = function(e) {
      document.getElementById('profilePicture').src = e.target.result;
    };
    reader.readAsDataURL(file);
  });
  
  function editProfile() {
    var bio = prompt("Enter your bio:", "{{ user.bio }}");
    if (bio !== null) {
      document.getElementById('bio').textContent = bio;
      // Update the bio in the backend (e.g., using AJAX or submitting a form)
    }
  }