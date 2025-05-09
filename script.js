const loginModal = document.getElementById("loginModal");
const signupModal = document.getElementById("signupModal");
const profileBtn = document.querySelector(".profile-btn");

profileBtn.addEventListener("click", () => {
  loginModal.style.display = "flex";
});

window.addEventListener("click", (e) => {
  if (e.target === loginModal) loginModal.style.display = "none";
  if (e.target === signupModal) signupModal.style.display = "none";
});

function togglePassword() {
  const input = document.getElementById("password");
  input.type = input.type === "password" ? "text" : "password";
}

// Switch from login to signup
document.querySelector(".signup-text a").addEventListener("click", (e) => {
  e.preventDefault();
  loginModal.style.display = "none";
  signupModal.style.display = "flex";
});

function switchToLogin() {
  signupModal.style.display = "none";
  loginModal.style.display = "flex";
}
