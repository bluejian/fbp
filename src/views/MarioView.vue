<template>
  <div class="mario-world" ref="mainContainer">
    <!-- BGM Controller -->
    <div class="bgm-bar" :class="{ active: bgmPlaying }" @click="toggleBgm">
      <div class="bgm-icon">
        <svg v-if="bgmPlaying" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18">
          <path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55C7.79 13 6 14.79 6 17s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/>
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18">
          <path d="M4.34 2.93L2.93 4.34 7.29 8.7 7 9H3v6h4l5 5v-6.59l4.18 4.18c-.65.49-1.38.88-2.18 1.11v2.06c1.34-.3 2.57-.97 3.56-1.88l2.1 2.1 1.41-1.41L4.34 2.93zM19 12c0 .82-.15 1.61-.41 2.34l1.53 1.53c.56-1.17.88-2.48.88-3.87 0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zm-7-8l-1.88 1.88L12 7.76zm4.5 8c0-1.77-1.02-3.29-2.5-4.03v1.79l2.48 2.48c.01-.08.02-.16.02-.24z"/>
        </svg>
      </div>
      <div class="bgm-eq" v-if="bgmPlaying"><span></span><span></span><span></span><span></span></div>
      <div class="bgm-label">{{ bgmPlaying ? 'Super Mario Bros.' : 'TAP TO PLAY' }}</div>
      <audio ref="bgmAudio" loop><source src="/audio/spmario.mp4" type="audio/mpeg"></audio>
    </div>

    <!-- ============ SCENE 1: GROUND (World 1-1) ============ -->
    <section class="scene scene-ground" id="scene1">
      <div class="sticky-frame">
        <!-- Wallpaper BG -->
        <div class="ground-bg" :style="{ backgroundPositionX: `${-stageOffset}vw` }"></div>

        <!-- HUD -->
        <div class="hud">
          <div><span>MARIO</span><br/><span>260307</span></div>
          <div><span>WORLD</span><br/><span>1-1</span></div>
        </div>

        <!-- Title (fades out) -->
        <div class="title-card" :style="{ opacity: 1 - scrollP1 * 2 }">
          <h1>JIAN'S 1ST<br/>BIRTHDAY</h1>
          <p class="blink-text">SCROLL TO START</p>
        </div>

        <!-- Stage elements (scroll with stageOffset) -->
        <div class="stage-track" :style="{ transform: `translateX(${-stageOffset}vw)` }">
          <!-- <img :src="getImg('/images/mario/mushroom.webp')" class="sprite" style="left:80vw; bottom:42%; width:50px;" /> -->
          <div class="block-row" style="left:190vw; bottom:50%;">
            <img :src="getImg('/images/mario/mario-brick.png')" class="sprite blk" />
            <img :src="getImg('/images/mario/mario-q-block.png')" class="sprite blk q-glow" />
            <img :src="getImg('/images/mario/mario-brick.png')" class="sprite blk" />
          </div>
          <div class="block-row" style="left:235vw; bottom:78%;">
            <img :src="getImg('/images/mario/mario-brick.png')" class="sprite blk" />
            <img :src="getImg('/images/mario/mario-q-block.png')" class="sprite blk q-glow" />
            <img :src="getImg('/images/mario/mario-brick.png')" class="sprite blk" />
          </div>
          <img :src="getImg('/images/mario/mushroom.webp')" class="sprite" style="left:236vw; bottom:87%; width:45px;" />
          <!-- Pipe on the ground -->
          <div class="ground-pipe" style="left:290vw; bottom: 30%">
            <img :src="getImg('/images/mario/mario-pipe.png')" class="sprite pipe-img" />
          </div>
        </div>
      </div>
    </section>

    <!-- ============ SCENE 2: UNDERGROUND (? Block Gallery) ============ -->
    <section class="scene scene-underground" id="scene2">
      <!-- 
        Global Scroll Snapping points for Scene 2. 
        Top is calculated to be the exact point where scrollP2 reaches 0.75 (Pause phase) for each block.
      -->
      <div v-for="i in photos.length" :key="'snap-'+i" class="snap-point"
           :style="{ top: `${((i - 1 + 0.7) / photos.length) * 300}vh` }"></div>

      <div class="sticky-frame underground-frame">
        <div class="underground-bg"></div>
        <div class="scene-label">UNDERGROUND GALLERY</div>

        <!-- HUD: World 1-2 (Underground) -->
        <div class="hud">
          <div><span>MARIO</span><br/><span>260307</span></div>
          <div><span>WORLD</span><br/><span>1-2</span></div>
        </div>

        <!-- ? Blocks row: scrolls horizontally, one per photo -->
        <div class="q-track" :style="{ transform: `translateX(${-undergroundOffset}vw)` }">
          <div
            v-for="(photo, i) in photos"
            :key="i"
            class="q-station"
            :style="{ left: `${150 + i * 80}vw` }"
          >
            <!-- Photo (appears ABOVE block when hit) -->
            <Transition name="photo-pop">
              <div v-if="hitBlocks[i]" class="revealed-photo" @click="openModal(i)">
                <img :src="photo" />
              </div>
            </Transition>
            <!-- ? Block (Mario hits from below) -->
            <div class="q-box" :class="{ hit: hitBlocks[i], idle: !hitBlocks[i] }">
              <img v-if="!hitBlocks[i]" :src="getImg('/images/mario/mario-q-block.png')" class="q-img" />
              <img v-else :src="getImg('/images/mario/mario-brick.png')" class="q-img" />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ SCENE 3: STAGE CLEAR ============ -->
    <section class="scene scene-clear" id="scene3">
      <div class="sticky-frame clear-frame">
        <div class="clear-bg"></div>

        <Transition name="pixel-pop">
          <div v-if="showClear" class="clear-card">
            <div class="clear-title">🎉 STAGE CLEAR!</div>

            <div class="clear-details">
              <p><strong>DATE:</strong> {{ eventDate }}</p>
              <p><strong>LOC:</strong> {{ venueName }}</p>
            </div>

            <!-- Parking Info Carousel -->
            <div class="parking-block">
              <div class="parking-title">🅿️ PARKING INFO</div>
              <div class="parking-carousel">
                <button class="arrow-btn" @click="prevParking">◀</button>
                <div class="carousel-img-wrap">
                  <img :src="parkingPhotos[parkingIndex]" @click="openParkingModal(parkingIndex)" />
                  <div class="page-dots">
                    <span v-for="(p, i) in parkingPhotos" :key="'dot-'+i" :class="{ active: i === parkingIndex }"></span>
                  </div>
                </div>
                <button class="arrow-btn" @click="nextParking">▶</button>
              </div>
            </div>

            <div class="map-buttons">
              <a :href="kakaoMapUrl" target="_blank" class="pixel-btn kakao">KAKAO MAP</a>
              <a :href="naverMapUrl" target="_blank" class="pixel-btn naver">NAVER MAP</a>
            </div>

            <div class="creator-stamp">CREATED BY JIAN'S FAMILY</div>
          </div>
        </Transition>
      </div>
    </section>

    <!-- ============ JIAN-MARIO (fixed character) ============ -->
    <div class="mario-fixed" :class="[{ walking: isWalking && !inPipe }, activeSceneClass]">
      <div class="mario-char" :style="marioStyle">
        <img :src="getImg('/images/mario/jianmario.png')" alt="Jian-Mario" />
      </div>
    </div>

    <!-- Photo Modal -->
    <div v-if="modalOpen" class="modal-overlay" @click="closeModal">
      <button class="nav-btn prev-btn" @click.stop="prevPhoto" v-if="modalList.length > 1">◀</button>
      
      <div class="modal-content" @click.stop>
        <img :src="modalSrc" />
        <div class="modal-hint" @click="closeModal">TAP TO CLOSE</div>
      </div>

      <button class="nav-btn next-btn" @click.stop="nextPhoto" v-if="modalList.length > 1">▶</button>
    </div>
  </div>
</template>

<script setup>
import { getImg } from '../utils/imagePath'
import { ref, computed, onMounted, onUnmounted } from 'vue'

// ===== DATA =====
const score = ref(120307)
const eventDate = ref('2026.03.07 18:00')
const venueName = ref('Ruel Party Place')
const kakaoMapUrl = 'https://map.kakao.com/link/to/236178717'
const naverMapUrl = 'https://naver.me/GOPeemGQ'

const photos = ref([
  getImg('/images/boxjian.jpeg'),
  getImg('/images/angjian.jpeg'),
  getImg('/images/boojian.jpeg'),
  getImg('/images/smilejian.jpeg'),
  getImg('/images/angryjian.jpeg'),
  getImg('/images/jiansmile.jpeg')
])

const parkingPhotos = ref([
  getImg('/images/mario/parking1.png'),
  getImg('/images/mario/parking2.jpg')
])
const parkingIndex = ref(0)
const nextParking = () => {
  parkingIndex.value = (parkingIndex.value + 1) % parkingPhotos.value.length
}
const prevParking = () => {
  parkingIndex.value = (parkingIndex.value - 1 + parkingPhotos.value.length) % parkingPhotos.value.length
}

// ===== SCROLL STATE =====
const scrollP1 = ref(0) // Scene 1 progress (0→1)
const scrollP2 = ref(0) // Scene 2 progress (0→1)
const scrollP3 = ref(0) // Scene 3 progress (0→1)

// ===== STAGE OFFSETS =====
const PIPE_AT = 0.90 // Progress where pipe reaches center (near end)
const MAX_OFFSET = 250 // Max horizontal scroll in vw (more travel)

const stageOffset = computed(() => {
  const p = scrollP1.value
  if (p <= PIPE_AT) return (p / PIPE_AT) * MAX_OFFSET
  return MAX_OFFSET
})

// ===== SCENE 2: Per-block sub-phases =====
// Each block gets 1/N of total scrollP2 range
// Within each block's slice:
//   0.00 - 0.35 = APPROACH (walk toward block)
//   0.35 - 0.50 = JUMP UP (Mario rises)
//   0.50 - 0.60 = PEAK (head hits block → block changes)
//   0.60 - 0.75 = LAND (Mario comes down, photo reveals)
//   0.75 - 1.00 = PAUSE (photo visible, Mario stands)
const blockPhase = ref({ index: -1, phase: 'idle', jumpY: 0 })

const undergroundOffset = computed(() => {
  const n = photos.value.length
  if (n === 0) return 0
  
  // First block needs 100vw of travel (since Mario sits at 50vw and block is at 150vw)
  const initialTravel = 100 
  // Subsequent blocks are 80vw apart
  const spacing = 80 
  
  let offset = 0
  for (let i = 0; i < n; i++) {
    const blockStart = i / n
    const blockEnd = (i + 1) / n
    if (scrollP2.value <= blockStart) break
    
    const blockProgress = Math.min((scrollP2.value - blockStart) / (blockEnd - blockStart), 1)
    // Only advance offset during APPROACH phase (0 to 0.35)
    const approachProgress = Math.min(blockProgress / 0.35, 1)
    
    const travelForThisBlock = (i === 0) ? initialTravel : spacing
    offset += approachProgress * travelForThisBlock
  }
  return offset
})

// ===== MARIO STATE =====
const marioX = ref(0)
const marioY = ref(0)
const isWalking = ref(false)
const isJumping = ref(false)

// Pipe entry state (only during Scene 1 pipe phase, not during Scene 2+)
const inPipe = computed(() => scrollP1.value > PIPE_AT && scrollP2.value === 0)

// Mario computed style
const marioStyle = computed(() => {
  if (inPipe.value) {
    const pipeP = (scrollP1.value - PIPE_AT) / (1 - PIPE_AT)
    return {
      transform: `translateX(0px) translateY(${pipeP * 250}px) scale(${1 - pipeP * 0.5})`,
      opacity: 1 - pipeP
    }
  }
  let currentOpacity = 1
  if (scrollP3.value > 0) {
    // Fade out Mario completely during the first 10% of Scene 3
    currentOpacity = Math.max(1 - (scrollP3.value / 0.1), 0)
  }

  return {
    transform: `translateX(${marioX.value}px) translateY(${-marioY.value}px)`,
    opacity: currentOpacity
  }
})

// ===== ? BLOCK HITS =====
const hitBlocks = ref([])
const showClear = ref(false)

// ===== BGM =====
const bgmPlaying = ref(false)
const bgmAudio = ref(null)
const toggleBgm = () => {
  if (bgmPlaying.value) bgmAudio.value.pause()
  else bgmAudio.value.play().catch(() => {})
  bgmPlaying.value = !bgmPlaying.value
}

// ===== MODAL =====
const modalOpen = ref(false)
const modalList = ref([])
const modalIndex = ref(0)
const modalSrc = computed(() => modalList.value[modalIndex.value])

// Teleport the background scroll to the current photo's block
const scrollToPhoto = (index) => {
  if (photos.value !== modalList.value) return // Only teleport for main gallery
  
  const vh = window.innerHeight
  // Scene 2 starts at vh * 6
  const s2 = vh * 6
  // Scene 2 scroll length is vh * 3
  const s2Length = vh * 3
  
  const n = photos.value.length
  // Target scrollP2 is at the end of the 'land' phase of the target block
  // approach + jump + peak + land = 0.75 of the block's scroll phase
  const targetP2 = (index / n) + (0.75 / n)
  
  const targetY = s2 + (targetP2 * s2Length)
  window.scrollTo({ top: targetY, behavior: 'instant' })
}

const openModal = (i) => { 
  modalList.value = photos.value; 
  modalIndex.value = i; 
  modalOpen.value = true 
}
const openParkingModal = (i) => { 
  modalList.value = parkingPhotos.value; 
  modalIndex.value = i; 
  modalOpen.value = true 
}
const closeModal = () => { modalOpen.value = false }

const nextPhoto = () => {
  if (modalIndex.value < modalList.value.length - 1) modalIndex.value++
  else modalIndex.value = 0
  scrollToPhoto(modalIndex.value)
}
const prevPhoto = () => {
  if (modalIndex.value > 0) modalIndex.value--
  else modalIndex.value = modalList.value.length - 1
  scrollToPhoto(modalIndex.value)
}

const handleKeydown = (e) => {
  if (!modalOpen.value) return
  if (e.key === 'ArrowRight') nextPhoto()
  if (e.key === 'ArrowLeft') prevPhoto()
  if (e.key === 'Escape') closeModal()
}

// Active Scene for CSS
const activeSceneClass = computed(() => {
  if (scrollP3.value > 0) return 'in-scene3'
  if (scrollP2.value > 0) return 'in-scene2'
  return 'in-scene1'
})

// ===== SCROLL HANDLER =====
const handleScroll = () => {
  const y = window.scrollY
  const vh = window.innerHeight

  // Scene 1: 600vh tall, sticky for 500vh
  scrollP1.value = Math.min(Math.max(y / (vh * 5), 0), 1)

  // Scene 2: 400vh tall, sticky for 300vh (faster scroll speed)
  const s2 = vh * 6
  scrollP2.value = Math.min(Math.max((y - s2) / (vh * 3), 0), 1)

  // Scene 3: starts after Scene 2 (600vh + 400vh = 1000vh)
  const s3 = vh * 10
  scrollP3.value = Math.min(Math.max((y - s3) / (vh * 2), 0), 1)

  // === SCENE 1: Mario X movement ===
  if (scrollP1.value > 0 && scrollP1.value <= PIPE_AT) {
    const norm = scrollP1.value / PIPE_AT
    marioX.value = (norm * 80) - 40
    isWalking.value = true
  } else if (inPipe.value) {
    marioX.value = 0
    isWalking.value = false
  }
  // === SCENE 2: Per-block state machine ===
  else if (scrollP2.value > 0 && scrollP2.value < 1) {
    const n = photos.value.length
    const currentBlock = Math.min(Math.floor(scrollP2.value * n), n - 1)
    const blockStart = currentBlock / n
    const blockEnd = (currentBlock + 1) / n
    const sub = (scrollP2.value - blockStart) / (blockEnd - blockStart) // 0→1 within block

    marioX.value = 0

    if (sub < 0.35) {
      // APPROACH: walking
      blockPhase.value = { index: currentBlock, phase: 'approach', jumpY: 0 }
      isWalking.value = true
      marioY.value = 0
    } else if (sub < 0.50) {
      // JUMP UP
      const jumpProgress = (sub - 0.35) / 0.15
      marioY.value = jumpProgress * 60
      blockPhase.value = { index: currentBlock, phase: 'jump', jumpY: marioY.value }
      isWalking.value = false
    } else if (sub < 0.60) {2
      // PEAK — head touches block
      marioY.value = 60
      hitBlocks.value[currentBlock] = true
      blockPhase.value = { index: currentBlock, phase: 'peak', jumpY: 60 }
      isWalking.value = false
    } else if (sub < 0.75) {
      // LAND — Mario comes down, photo reveals
      const landProgress = (sub - 0.60) / 0.15
      marioY.value = 60 * (1 - landProgress)
      hitBlocks.value[currentBlock] = true
      blockPhase.value = { index: currentBlock, phase: 'land', jumpY: marioY.value }
      isWalking.value = false
    } else {
      // PAUSE — photo fully visible, Mario standing
      marioY.value = 0
      hitBlocks.value[currentBlock] = true
      blockPhase.value = { index: currentBlock, phase: 'pause', jumpY: 0 }
      isWalking.value = false
    }

    // Reset blocks that are ahead of current scroll position (scroll back)
    for (let i = currentBlock + 1; i < n; i++) {
      hitBlocks.value[i] = false
    }
    // If we scrolled back before peak on current block, un-hit it
    if (sub < 0.50) {
      hitBlocks.value[currentBlock] = false
    }
  }
  // === SCENE 3 ===
  else if (scrollP3.value > 0) {
    isWalking.value = false
    marioX.value = 0
    
    // Smoothly lower Mario down into the bottom of the screen (150px down)
    const lowerProgress = Math.min(scrollP3.value / 0.15, 1)
    marioY.value = -(lowerProgress * 150)

    if (scrollP3.value > 0.3 && !showClear.value) {
      showClear.value = true
    }
  } else {
    isWalking.value = false
  }

  // Walking timeout
  if (isWalking.value) {
    clearTimeout(window._wt)
    window._wt = setTimeout(() => { isWalking.value = false }, 150)
  }
}

const triggerJump = () => {
  if (isJumping.value) return
  isJumping.value = true
  marioY.value = 80
  setTimeout(() => { marioY.value = 0; isJumping.value = false }, 350)
}

// ===== LIFECYCLE =====
onMounted(() => {
  hitBlocks.value = new Array(photos.value.length).fill(false)
  window.addEventListener('scroll', handleScroll)
  window.addEventListener('keydown', handleKeydown)
})
onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
@font-face {
  font-family: 'DungGeunMo';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/DungGeunMo.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

/* ===== BASE ===== */
.mario-world {
  background: #000;
  font-family: 'Press Start 2P', 'DungGeunMo', cursive;
  color: #fff;
  text-transform: uppercase;

  /* ===== MARIO BOTTOM SETTINGS ===== */
  /* 단말기 세로 길이에 비례하도록 px 대신 vh를 사용해 어떤 모바일화면이든 바닥에 붙도록 변경합니다 */
  --mario-bottom-s1: 28vh;    /* Scene 1: 그라운드 위 위치 (약 20~25vh) */
  --mario-bottom-s2: 15vh;    /* Scene 2: 지하 갤러리 위치 */
  --mario-bottom-s3: 15vh;    /* Scene 3: 클리어 화면 (스크롤시 추가 하강됨) */
  --mario-height: 130px;      /* 데스크탑 마리오 캐릭터 높이 */
}

/* 픽셀 폰트는 굵은(bold) 글자체를 지원하지 않아 폰트가 깨질 수 있습니다. 강제로 normal 적용 */
.mario-world strong, .mario-world b, .mario-world h1 {
  font-weight: normal;
}

.scene { position: relative; }
.scene-ground { height: 600vh; background: #5c94fc; z-index: 1; }
.scene-underground { height: 400vh; background: #1a0a2e; position: relative; z-index: 2; }
.scene-clear { height: 300vh; background: #0a0a1a; position: relative; z-index: 3; }

.sticky-frame {
  position: sticky; top: 0;
  height: 100vh; width: 100%;
  overflow: hidden;
}

/* ===== SCENE 1: GROUND ===== */
.ground-bg {
  position: absolute;
  left: 0; right: 0; bottom: 0;
  height: 60%;
  background-image: url('/images/mario/wallpapaer.avif');
  background-size: auto 100%;
  background-repeat: repeat-x;
  image-rendering: pixelated;
}

.hud {
  position: absolute; top: 50px; width: 100%;
  display: flex; justify-content: space-between; padding: 0 30px;
  font-size: 0.6rem; line-height: 1.6; z-index: 10;
}

.title-card {
  position: absolute; inset: 0;
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  z-index: 10; text-align: center; padding: 0 20px;
  margin-bottom: 120px;
}
.title-card h1 { font-size: 1.8rem; text-shadow: 4px 4px #c80000; line-height: 1.5; margin-bottom: 16px; }
.blink-text { font-size: 0.55rem; color: #ffff00; animation: blink 1.2s infinite alternate; }
@keyframes blink { from { opacity: 0.2; } to { opacity: 1; } }

.stage-track {
  position: absolute; inset: 0;
  width: 300vw;
  pointer-events: none;
}
.sprite { position: absolute; image-rendering: pixelated; }
.blk { width: 60px; height: 60px; }
.block-row { display: flex; gap: 0; position: absolute; }
.block-row .sprite { position: relative; } /* Override absolute so flex works */

.q-glow {
  animation: qPulse 1.5s infinite alternate;
  filter: drop-shadow(0 0 8px rgba(255,200,0,0.6));
}
@keyframes qPulse {
  0% { filter: drop-shadow(0 0 4px rgba(255,200,0,0.3)); }
  100% { filter: drop-shadow(0 0 14px rgba(255,200,0,0.9)); }
}

/* Pipe on ground level */
.ground-pipe {
  position: absolute;
  bottom: 36%;
  transform: translateX(-50%);
}
.pipe-img { width: 110px; height: auto; }

/* ===== SCENE 2: UNDERGROUND ===== */
.underground-frame {
  display: flex; flex-direction: column;
  justify-content: center; align-items: center;
  background: #1a0a2e;
}
.underground-bg {
  position: absolute; inset: 0;
  background:
    repeating-linear-gradient(0deg, rgba(255,255,255,0.015) 0px, rgba(255,255,255,0.015) 1px, transparent 1px, transparent 24px),
    repeating-linear-gradient(90deg, rgba(255,255,255,0.015) 0px, rgba(255,255,255,0.015) 1px, transparent 1px, transparent 24px);
}
.scene-label {
  position: absolute; top: 60px;
  font-size: 0.65rem; color: #00ffff; letter-spacing: 2px; z-index: 5;
}

.q-track {
  position: absolute; inset: 0;
  width: 500vw;
  pointer-events: none;
}

.q-station {
  position: absolute;
  /* Block bottom height automatically calculated: 
     Mario Bottom + Mario Height + Jump Height (60px) */
  bottom: calc(var(--mario-bottom-s2) + var(--mario-height) + 60px);
  transform: translateX(-50%); /* Perfectly center the block */
  display: flex; flex-direction: column;
  align-items: center;
  pointer-events: auto;
}
.q-box {
  width: 70px; height: 70px;
  transition: transform 0.2s;
}
.q-box.hit {
  animation: blockHit 0.3s ease-out;
}
@keyframes blockHit {
  0% { transform: translateY(0); }
  40% { transform: translateY(-30px); }
  100% { transform: translateY(0); }
}
.q-box.idle .q-img {
  animation: qFloat 2s infinite ease-in-out;
}
@keyframes qFloat {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-5px); }
}
.q-img { width: 100%; height: 100%; image-rendering: pixelated; }

/* Revealed photo — pops UP above the block */
.revealed-photo {
  margin-bottom: 30px;
  width: 250px; height: 250px;
  border: 4px solid rgba(255,255,255,0.4);
  border-radius: 6px;
  overflow: hidden;
  cursor: pointer;
  pointer-events: auto;
  box-shadow: 0 4px 20px rgba(0,255,255,0.15);
}
.revealed-photo img {
  width: 100%; height: 100%; object-fit: cover;
}
.photo-pop-enter-active {
  animation: photoReveal 0.5s ease-out;
}
@keyframes photoReveal {
  0% { transform: translateY(30px) scale(0.5); opacity: 0; }
  60% { transform: translateY(-10px) scale(1.05); opacity: 1; }
  100% { transform: translateY(0) scale(1); opacity: 1; }
}

/* ===== SCENE 3: STAGE CLEAR ===== */
.clear-frame {
  display: flex; justify-content: center; align-items: center;
  background: linear-gradient(180deg, #1a0a2e 0%, #0d0d2b 100%);
}
.clear-bg {
  position: absolute; inset: 0;
  background: radial-gradient(circle at 50% 30%, rgba(255,200,0,0.05) 0%, transparent 60%);
}

.clear-card {
  position: relative; z-index: 10;
  width: 90%; max-width: 400px;
  background: #fff; color: #333;
  border: 5px solid #222; border-radius: 6px;
  padding: 24px; text-align: center;
  box-shadow: 8px 8px rgba(255,0,0,0.6);
}
.clear-title {
  font-size: 0.85rem; color: #e60000;
  margin-bottom: 16px; padding-bottom: 12px;
  border-bottom: 3px solid #eee;
}
.clear-details {
  font-size: 0.55rem; line-height: 2.2;
  text-align: left; margin-bottom: 16px;
}
.creator-stamp {
  margin-top: 24px;
  font-size: 0.45rem;
  color: #999;
}

/* Parking block */
.parking-block {
  background: #f5f5f5; border: 3px solid #ddd;
  border-radius: 4px; padding: 14px;
  margin-bottom: 16px;
}
.parking-title {
  font-size: 0.5rem; color: #555;
  margin-bottom: 10px;
}
.parking-carousel {
  display: flex; align-items: center; justify-content: space-between; gap: 8px;
}
.arrow-btn {
  background: #eee; border: 2px solid #ccc; border-radius: 4px;
  color: #555; padding: 8px 6px; cursor: pointer; font-size: 0.5rem;
  transition: transform 0.1s, background 0.2s;
}
.arrow-btn:active { transform: scale(0.9); background: #ddd; }

.carousel-img-wrap {
  flex-grow: 1; display: flex; flex-direction: column; align-items: center;
}
.carousel-img-wrap img {
  width: 100%; max-height: 160px;
  object-fit: cover; border-radius: 4px;
  border: 2px solid #ccc; cursor: pointer;
}
.page-dots {
  display: flex; gap: 4px; margin-top: 8px;
}
.page-dots span {
  width: 6px; height: 6px; border-radius: 50%; background: #ccc;
}
.page-dots span.active { background: #555; }

.map-buttons { display: flex; flex-direction: row; gap: 10px; justify-content: center;}
.pixel-btn {
  display: block; padding: 13px; text-decoration: none;
  font-family: 'Press Start 2P', cursive;
  font-size: 0.5rem; color: #fff;
  border: 3px solid #000; text-align: center; border-radius: 3px;
  transition: transform 0.15s;
}
.pixel-btn:active { transform: scale(0.95); }
.kakao { background: #FEE500; width: 100%; }
.naver { background: #33A11D; width: 100%; }

.pixel-pop-enter-active { animation: popIn 0.5s ease-out; }
@keyframes popIn {
  0% { transform: scale(0.3); opacity: 0; }
  70% { transform: scale(1.05); }
  100% { transform: scale(1); opacity: 1; }
}

/* ===== JIAN-MARIO (FIXED) ===== */
.mario-fixed {
  position: fixed;
  left: 50%;
  transform: translateX(-50%);
  z-index: 5; /* Lowered from 1000 so clear-card (z-10) covers it */
  pointer-events: none;
  transition: bottom 0.3s ease-in-out; /* Smooth transition between scenes */
}
.mario-fixed.in-scene1 { bottom: var(--mario-bottom-s1); }
.mario-fixed.in-scene2 { bottom: var(--mario-bottom-s2); }
.mario-fixed.in-scene3 { bottom: var(--mario-bottom-s3); }

.mario-char {
  width: 110px; height: var(--mario-height);
  transition: transform 0.08s linear;
}
.mario-char img {
  width: 100%; height: 100%;
  object-fit: contain;
  image-rendering: pixelated;
}
.walking .mario-char {
  animation: walkBob 0.22s infinite steps(2);
}
@keyframes walkBob {
  0% { transform: translateY(0); }
  50% { transform: translateY(-4px); }
}

/* ===== MODAL ===== */
.modal-overlay {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.92);
  z-index: 5000;
  display: flex; align-items: center; justify-content: space-between;
  padding: 20px;
}
.modal-content {
  text-align: center; max-width: 80%; flex-grow: 1;
}
.modal-content img {
  width: 100%; max-height: 80vh;
  object-fit: contain; border-radius: 4px;
  border: 3px solid rgba(255,255,255,0.2);
}
.modal-hint {
  font-size: 0.45rem; color: rgba(255,255,0,0.5);
  margin-top: 12px; cursor: pointer;
}
.nav-btn {
  background: none; border: none; color: rgba(255,255,255,0.5);
  font-size: 2rem; padding: 20px; cursor: pointer;
  transition: color 0.2s, transform 0.2s;
  z-index: 5010; flex-shrink: 0;
}
.nav-btn:hover { color: #fff; transform: scale(1.1); }
.nav-btn:active { transform: scale(0.9); }

/* ===== BGM BAR ===== */
.bgm-bar {
  position: fixed; top: 14px; right: 14px; z-index: 2100;
  display: flex; align-items: center; gap: 7px;
  background: rgba(0,0,0,0.5);
  backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
  padding: 7px 12px; border-radius: 24px;
  cursor: pointer; color: rgba(255,255,255,0.65);
  border: 1px solid rgba(255,255,255,0.08);
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}
.bgm-bar.active { border-color: rgba(255,200,0,0.25); color: #ffcc00; }
.bgm-icon { display: flex; align-items: center; flex-shrink: 0; }
.bgm-label { font-size: 9px; letter-spacing: 0.4px; white-space: nowrap; }
.bgm-eq { display: flex; align-items: flex-end; gap: 2px; height: 12px; }
.bgm-eq span {
  display: block; width: 2.5px; background: #ffcc00; border-radius: 1px;
  animation: eqB 0.6s infinite ease-in-out alternate;
}
.bgm-eq span:nth-child(1) { height: 5px; animation-delay: 0s; }
.bgm-eq span:nth-child(2) { height: 9px; animation-delay: 0.15s; }
.bgm-eq span:nth-child(3) { height: 3px; animation-delay: 0.3s; }
.bgm-eq span:nth-child(4) { height: 7px; animation-delay: 0.45s; }
@keyframes eqB { 0% { height: 2px; } 100% { height: 12px; } }

/* ===== MOBILE ===== */
@media (max-width: 768px) {
  .mario-world {
    /* 모바일에서도 동일하게 vh 비율을 기반으로 잡습니다 */
    --mario-bottom-s1: 28vh;
    --mario-bottom-s2: 15vh;
    --mario-bottom-s3: 15vh;
    --mario-height: 85px;
  }
  .title-card h1 { font-size: 1.2rem; }
  .blink-text { font-size: 0.45rem; }
  .hud { top: 40px; padding: 0 16px; font-size: 0.45rem; }
  .mario-char { width: 70px; height: 85px; }
  .mario-fixed { bottom: 45px; }
  .blk { width: 45px; height: 45px; }
  .pipe-img { width: 80px; }
  .q-box { width: 55px; height: 55px; }
  .revealed-photo { width: 250px; height: 250px; margin-bottom: 30px; }
  .scene-label { font-size: 0.5rem; top: 45px; }
  .clear-card { width: 92%; padding: 16px; }
  .clear-title { font-size: 0.7rem; }
  .clear-details { font-size: 0.45rem; line-height: 2.0; }
  .pixel-btn { padding: 11px; font-size: 0.43rem; }
  .map-buttons { flex-direction: column; } /* Stack map buttons on mobile */
  
  .parking-title { font-size: 0.43rem; }
  .bgm-bar { top: 10px; right: 10px; padding: 5px 9px; }
  .bgm-label { font-size: 7.5px; }
  
  /* Modal fixes for mobile */
  .modal-content { max-width: 90%; }
  .nav-btn { font-size: 1.2rem; padding: 10px; }
}

@media (max-width: 375px) {
  .mario-world {
    --mario-height: 68px;
  }
  .title-card h1 { font-size: 1rem; }
  .mario-char { width: 56px; height: 68px; }
  .blk { width: 38px; height: 38px; }
  .pipe-img { width: 65px; }
  .q-box { width: 45px; height: 45px; }
  .revealed-photo { width: 200px; height: 200px; margin-bottom: 25px; }
}
</style>

<style>
/* 
  Global scroll snap to "catch" the scroll when the photo opens.
  It softly snaps when the user scrolls near a .snap-point.
*/
html, body {
  scroll-snap-type: y proximity;
}

.snap-point {
  position: absolute;
  width: 100%;
  height: 1px;
  scroll-snap-align: start;
  scroll-snap-stop: always; /* Forces the browser to stop here once */
  pointer-events: none;
  z-index: -1;
}
</style>
