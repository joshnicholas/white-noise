<script>
  import { onMount } from 'svelte';
  import { base } from '$app/paths';

  let { audioPath, title, isPlaying: propIsPlaying = false, volume: propVolume = 0.5, onPlayingChange, onVolumeChange } = $props();

  let audio = $state();
  let isPlaying = $state(propIsPlaying);
  let volume = $state(propVolume);
  let isLoaded = $state(false);
  let error = $state(null);

  $effect(() => {
    if (audio && isLoaded) {
      if (propIsPlaying && !isPlaying) {
        audio.play().then(() => {
          isPlaying = true;
        }).catch(() => {
          error = 'Failed to play audio';
          isPlaying = false;
        });
      } else if (!propIsPlaying && isPlaying) {
        audio.pause();
        isPlaying = false;
      }
    }
  });

  $effect(() => {
    volume = propVolume;
    if (audio) {
      audio.volume = volume;
    }
  });

  onMount(() => {
    if (audio) {
      audio.loop = true;
      audio.volume = volume;

      audio.addEventListener('loadeddata', () => {
        isLoaded = true;
        error = null;
      });

      audio.addEventListener('canplay', () => {
        isLoaded = true;
        error = null;
      });

      audio.addEventListener('error', (e) => {
        console.error('Audio error:', e);
        error = 'Failed to load audio file';
        isLoaded = false;
      });

      audio.addEventListener('ended', () => {
        isPlaying = false;
      });

      // Force load the audio
      audio.load();
    }
  });

  function togglePlayPause() {
    if (!audio || !isLoaded) return;

    if (isPlaying) {
      audio.pause();
      isPlaying = false;
      onPlayingChange?.(false);
    } else {
      audio.play().then(() => {
        isPlaying = true;
        onPlayingChange?.(true);
      }).catch(() => {
        error = 'Failed to play audio';
        isPlaying = false;
        onPlayingChange?.(false);
      });
    }
  }

  function handleVolumeChange(event) {
    volume = parseFloat(event.target.value);
    if (audio) {
      audio.volume = volume;
    }
    onVolumeChange?.(volume);
  }
</script>

<div class="w-full {isPlaying ? 'bg-[#ff5860]' : 'bg-[#F4BB44]'} max-w-md mx-auto rounded-lg p-6 space-y-4">
  <h2 class="text-xl font-semibold text-black text-center">{title}</h2>

  <audio bind:this={audio} preload="auto">
    <source src={base + audioPath} type="audio/mpeg">
    <source src={base + audioPath} type="audio/wav">
    <source src={base + audioPath} type="audio/ogg">
    Your browser does not support the audio element.
  </audio>

  {#if error}
    <div class="text-red-500 text-center text-sm">{error}</div>
  {/if}

  <div class="flex flex-col items-center space-y-4">
    <button
      onclick={togglePlayPause}
      disabled={!isLoaded}
      class="w-16 h-16 rounded-full flex items-center justify-center transition-all duration-200 {isLoaded ? 'bg-[#FFDB58]' : 'bg-gray-300'} text-[#ff8d00] disabled:cursor-not-allowed"
    >
      {#if !isLoaded}
        <div class="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
      {:else if isPlaying}
        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
          <path d="M6 4h4v16H6V4zm8 0h4v16h-4V4z"/>
        </svg>
      {:else}
        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24" style="margin-left: 2px;">
          <path d="M8 5v14l11-7z"/>
        </svg>
      {/if}
    </button>

    <div class="w-full space-y-2">
      <!-- <div class="flex items-center justify-between text-sm text-gray-600">
        <span>Volume</span>
        <span>{Math.round(volume * 100)}%</span>
      </div> -->
      <input
        type="range"
        min="0"
        max="1"
        step="0.01"
        value={volume}
        oninput={handleVolumeChange}
        class="w-full h-2 bg-[#FFDB58] rounded-lg appearance-none cursor-pointer slider"
      />
    </div>
  </div>
</div>

<style>
  .slider::-webkit-slider-thumb {
    appearance: none;
    height: 20px;
    width: 20px;
    border-radius: 50%;
    background: #ff8d00;
    cursor: pointer;

    transition: background .15s ease-in-out;
  }

  .slider::-webkit-slider-thumb:hover {
    background: #E6AC00;
  }

  .slider::-moz-range-thumb {
    height: 20px;
    width: 20px;
    border-radius: 50%;
    background: #ff8d00;
    cursor: pointer;
    border: none;

  }
</style>