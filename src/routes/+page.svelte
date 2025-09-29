<script>
  import WhiteNoisePlayer from '$lib/WhiteNoisePlayer.svelte';

  let currentSettings = $state({
    seaside: { isPlaying: false, volume: 0.5 },
    waves: { isPlaying: false, volume: 0.5 },
    rain: { isPlaying: false, volume: 0.5 },
    coffeeshop: { isPlaying: false, volume: 0.5 },
    vicmarket: { isPlaying: false, volume: 0.5 },
    statelibrary: { isPlaying: false, volume: 0.5 }
  });

  let selectedDefault = $state(null);

$effect(() =>{ console.log("currentSettings: ", currentSettings)})

  const defaultPresets = [
    {
      name: "Rainy cafe",
      settings: {
        seaside: { isPlaying: false, volume: 0.5 },
        waves: { isPlaying: false, volume: 0.5 },
        rain: { isPlaying: true, volume: 0.7 },
        coffeeshop: { isPlaying: true, volume: 0.3 },
        vicmarket: { isPlaying: false, volume: 0.5 },
        statelibrary: { isPlaying: false, volume: 0.5 }
      }
    },
    {
      name: "Rainy library",
      settings: {
        seaside: { isPlaying: false, volume: 0.5 },
        waves: { isPlaying: false, volume: 0.5 },
        rain: { isPlaying: true, volume: 0.5 },
        coffeeshop: { isPlaying: false, volume: 0.5 },
        vicmarket: { isPlaying: false, volume: 0.5 },
        statelibrary: { isPlaying: true, volume: 0.9 }
      }
    },
    {
      name: "Vic Market at the beach",
      settings: {
        seaside: { isPlaying: true, volume: 0.3 },
        waves: { isPlaying: true, volume: 0.4 },
        rain: { isPlaying: false, volume: 0.5 },
        coffeeshop: { isPlaying: false, volume: 0.5 },
        vicmarket: { isPlaying: true, volume: 0.9 },
        statelibrary: { isPlaying: false, volume: 0.5 }
      }
    }
  ];

  function applyDefault(presetName) {
    if (selectedDefault === presetName) {
      // Toggle off - stop all players
      currentSettings = {
        seaside: { isPlaying: false, volume: currentSettings.seaside.volume },
        waves: { isPlaying: false, volume: currentSettings.waves.volume },
        rain: { isPlaying: false, volume: currentSettings.rain.volume },
        coffeeshop: { isPlaying: false, volume: currentSettings.coffeeshop.volume },
        vicmarket: { isPlaying: false, volume: currentSettings.vicmarket.volume },
        statelibrary: { isPlaying: false, volume: currentSettings.statelibrary.volume }
      };
      selectedDefault = null;
    } else {
      // Apply new default
      const preset = defaultPresets.find(p => p.name === presetName);
      if (preset) {
        currentSettings = { ...preset.settings };
        selectedDefault = presetName;
      }
    }
  }

  function updatePlayerState(playerKey, field, value) {
    currentSettings[playerKey][field] = value;
  }

  function resetAll() {
    currentSettings = {
      seaside: { isPlaying: false, volume: 0.5 },
      waves: { isPlaying: false, volume: 0.5 },
      rain: { isPlaying: false, volume: 0.5 },
      coffeeshop: { isPlaying: false, volume: 0.5 },
      vicmarket: { isPlaying: false, volume: 0.5 },
      statelibrary: { isPlaying: false, volume: 0.5 }
    };
    selectedDefault = null;
  }
</script>

<div class="min-h-screen py-12 px-4">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-4xl font-bold text-center text-black mb-8">Nona Nona Nonaaaaaa</h1>

    <div class="flex justify-center gap-4 mb-8">
      {#each defaultPresets as preset}
        <button
          onclick={() => applyDefault(preset.name)}
          class="px-6 py-3 {selectedDefault === preset.name ? 'bg-[#ff5860]' : 'bg-[#F4BB44]'} text-black font-semibold rounded-lg transition-colors"
        >
          {preset.name}
        </button>
      {/each}
    </div>

    <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-2">

      <WhiteNoisePlayer
        audioPath="/audio/seaside.mp3"
        title="Seaside"
        isPlaying={currentSettings.seaside.isPlaying}
        volume={currentSettings.seaside.volume}
        onPlayingChange={(isPlaying) => updatePlayerState('seaside', 'isPlaying', isPlaying)}
        onVolumeChange={(volume) => updatePlayerState('seaside', 'volume', volume)}
      />
      <WhiteNoisePlayer
        audioPath="/audio/waves.mp3"
        title="Waves"
        isPlaying={currentSettings.waves.isPlaying}
        volume={currentSettings.waves.volume}
        onPlayingChange={(isPlaying) => updatePlayerState('waves', 'isPlaying', isPlaying)}
        onVolumeChange={(volume) => updatePlayerState('waves', 'volume', volume)}
      />

      <WhiteNoisePlayer
        audioPath="/audio/rain.mp3"
        title="Rain"
        isPlaying={currentSettings.rain.isPlaying}
        volume={currentSettings.rain.volume}
        onPlayingChange={(isPlaying) => updatePlayerState('rain', 'isPlaying', isPlaying)}
        onVolumeChange={(volume) => updatePlayerState('rain', 'volume', volume)}
      />

      <WhiteNoisePlayer
        audioPath="/audio/coffeeshop.mp3"
        title="Cafe"
        isPlaying={currentSettings.coffeeshop.isPlaying}
        volume={currentSettings.coffeeshop.volume}
        onPlayingChange={(isPlaying) => updatePlayerState('coffeeshop', 'isPlaying', isPlaying)}
        onVolumeChange={(volume) => updatePlayerState('coffeeshop', 'volume', volume)}
      />

            <WhiteNoisePlayer
        audioPath="/audio/vicmarket.mp3"
        title="Vic Market"
        isPlaying={currentSettings.vicmarket.isPlaying}
        volume={currentSettings.vicmarket.volume}
        onPlayingChange={(isPlaying) => updatePlayerState('vicmarket', 'isPlaying', isPlaying)}
        onVolumeChange={(volume) => updatePlayerState('vicmarket', 'volume', volume)}
      />

      <WhiteNoisePlayer
        audioPath="/audio/statelibrary.mp3"
        title="State Library"
        isPlaying={currentSettings.statelibrary.isPlaying}
        volume={currentSettings.statelibrary.volume}
        onPlayingChange={(isPlaying) => updatePlayerState('statelibrary', 'isPlaying', isPlaying)}
        onVolumeChange={(volume) => updatePlayerState('statelibrary', 'volume', volume)}
      />

    </div>

    <div class="flex justify-center mt-12">
      <button
        onclick={resetAll}
        class="px-8 py-3 bg-[#F4BB44] text-black font-semibold rounded-lg transition-colors"
      >
        Reset
      </button>
    </div>

    <!-- <div class="mt-12 text-center text-gray-600">
      <p>Place your audio files in the <code class="bg-gray-200 px-2 py-1 rounded">static/audio/</code> directory</p>
    </div> -->
  </div>
</div>


<!-- xattr -d com.apple.quarantine '/Users/josh/Downloads/State Library dome 1.m4a' -->