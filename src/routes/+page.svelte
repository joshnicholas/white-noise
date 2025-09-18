<script>
  import WhiteNoisePlayer from '$lib/WhiteNoisePlayer.svelte';
</script>

<div class="min-h-screen py-12 px-4">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-4xl font-bold text-center text-[#ff8d00] mb-8">Nona Player</h1>

    <div class="grid gap-8 md:grid-cols-2 lg:grid-cols-2">
      <WhiteNoisePlayer
        audioPath="/audio/seaside.mp3"
        title="Seaside"
      />
            <WhiteNoisePlayer
        audioPath="/audio/waves.mp3"
        title="Waves"
      />

      <WhiteNoisePlayer
        audioPath="/audio/rain.mp3"
        title="Rain"
      />

      <WhiteNoisePlayer
        audioPath="/audio/coffeeshop.mp3"
        title="Cafe"
      />

    </div>

    <!-- <div class="mt-12 text-center text-gray-600">
      <p>Place your audio files in the <code class="bg-gray-200 px-2 py-1 rounded">static/audio/</code> directory</p>
    </div> -->
  </div>
</div>
