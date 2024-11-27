document.addEventListener("DOMContentLoaded", function () {
    const audioPlayer = document.getElementById("audio-player");
    const playButton = document.getElementById("play-btn");
    const pauseButton = document.getElementById("pause-btn");
    const stopButton = document.getElementById("stop-btn");
    const songStatus = document.getElementById("song-status");

    // Play music
    playButton.addEventListener("click", function () {
        audioPlayer.play();
        songStatus.textContent = "Playing music...";
    });

    // Pause music
    pauseButton.addEventListener("click", function () {
        audioPlayer.pause();
        songStatus.textContent = "Music paused";
    });

    // Stop music
    stopButton.addEventListener("click", function () {
        audioPlayer.pause();
        audioPlayer.currentTime = 0;
        songStatus.textContent = "Music stopped";
    });
});
