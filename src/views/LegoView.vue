<template>
  <div class="lego-concept-theme">
    <div class="scroll-container">
      <!-- Instruction Manual Header -->
      <header class="manual-header-section reveal">
        <div class="manual-blue-strip">
          <div class="lego-logo-small">LEGO</div>
          <div class="item-id">Item: 2026-0307</div>
        </div>
        <div class="hero-box">
          <div class="manual-image-container">
             <img src="/images/lego-brand-bg.png" alt="LEGO" class="manual-bg" />
             <div class="manual-overlay-graphics">
                <div class="piece-count">1,000,000+ PCS</div>
                <div class="age-label">1+</div>
             </div>
          </div>
          <h1 class="project-title">THE JI-AN BIRTHDAY BUILD</h1>
          <div class="manual-subtitle">Building Instructions</div>
        </div>
      </header>

      <!-- Step 1: Greeting -->
      <section class="build-step reveal">
        <div class="step-marker">1</div>
        <div class="brick-plate white">
          <div class="plate-studs">
            <span v-for="n in 8" :key="n"></span>
          </div>
          <div class="plate-content">
            <p class="greeting-text">{{ message }}</p>
          </div>
        </div>
        <!-- Brick Piece Illustration -->
        <div class="floating-brick red-2x4"></div>
      </section>

      <!-- Step 2: Gallery Assembly -->
      <section class="build-step reveal">
        <div class="step-marker">2</div>
        <div class="instruction-grid-box">
           <h2 class="grid-title">ASSEMBLE THE MOMENTS</h2>
           <div class="gallery-bricks-grid">
             <div 
               v-for="(photo, index) in photos" 
               :key="index"
               class="photo-brick-assembly"
               @click="openModal(index)"
             >
               <div class="assembly-ghost-outline"></div>
               <div class="real-photo-brick" :style="{ backgroundImage: `url(${photo})` }">
                  <div class="stud-layer">
                    <span></span><span></span>
                  </div>
               </div>
               <div class="assembly-arrow"></div>
             </div>
           </div>
        </div>
      </section>

      <!-- Step 3: Location Point -->
      <section class="build-step reveal">
        <div class="step-marker">3</div>
        <div class="baseplate-info">
          <div class="plate-studs green-studs">
            <span v-for="n in 12" :key="n"></span>
          </div>
          <div class="info-details">
             <div class="detail-row">
                <div class="icon-brick">🕒</div>
                <div class="text">
                  <span class="lbl">DATE:</span> {{ eventDate }}
                </div>
             </div>
             <div class="detail-row">
                <div class="icon-brick">📍</div>
                <div class="text">
                  <span class="lbl">BASE:</span> {{ venueName }}
                </div>
             </div>
             
             <div class="map-assembly">
               <div class="map-preview">CONSTRUCTION SITE: RUELLE</div>
               <div class="lego-action-btns">
                 <a :href="kakaoMapUrl" target="_blank" class="brick-btn blue">NAVIGATE_KAKAOMAP</a>
                 <a :href="naverMapUrl" target="_blank" class="brick-btn green">NAVIGATE_NAVERMAP</a>
               </div>
             </div>
          </div>
        </div>
      </section>

      <footer class="lego-build-footer reveal">
        <div class="build-complete-stamp">BUILD COMPLETE</div>
        <div class="footer-bricks">
           <div class="b r"></div><div class="b y"></div><div class="b b"></div><div class="b g"></div>
        </div>
        <p class="copyright-humor">Ji-An Birthday Animation Studios</p>
      </footer>
    </div>

    <!-- Lego Modal -->
    <Teleport to="body">
      <Transition name="brick-snap">
        <div v-if="modalOpen" class="lego-modal" @click="modalOpen = false">
           <div class="modal-brick-case">
              <div class="modal-studs"><span></span><span></span><span></span><span></span></div>
              <img :src="photos[currentIndex]" class="modal-photo" />
              <div class="modal-bottom-studs"><span></span><span></span><span></span><span></span></div>
              <div class="close-btn">CLICK TO DISASSEMBLE</div>
           </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const message = ref(`EVERYTHING IS AWESOME!\n\n지안이의 첫해 조립이 드디어 완성되었습니다.\n함께 오셔서 마지막 브릭 하나를 채워주시고\n지안이의 멋진 성장을 축하해주세요!`)
const eventDate = ref('2026.03.07 SAT PM 6:00')
const venueName = ref('루엘 파티플레이스')
const photos = ref(['/images/photo1.jpg', '/images/photo2.jpg', '/images/photo3.jpg', '/images/photo4.jpg'])
const kakaoMapUrl = 'https://map.kakao.com/link/to/236178717'
const naverMapUrl = 'https://naver.me/GOPeemGQ'

const modalOpen = ref(false)
const currentIndex = ref(0)
const openModal = (i) => { currentIndex.value = i; modalOpen.value = true }

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible') })
  }, { threshold: 0.1 })
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el))
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&family=Montserrat:wght@900&display=swap');

.lego-concept-theme {
  background: #dbdce0; /* Lego Grey surface */
  min-height: 100vh;
  display: flex;
  justify-content: center;
  font-family: 'Luckiest Guy', cursive;
  color: #333;
}

.scroll-container {
  width: 100%;
  max-width: 500px;
  background: #fff;
  position: relative;
  box-shadow: 0 0 50px rgba(0,0,0,0.1);
}

.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Manual Header */
.manual-header-section { border-bottom: 8px solid #DBE1E7; }
.manual-blue-strip {
  background: #0055BF;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #fff;
}
.lego-logo-small { font-family: 'Montserrat', sans-serif; font-weight: 900; background: #E3000B; padding: 2px 5px; border: 2px solid #fff; font-size: 0.8rem; }
.item-id { font-size: 0.7rem; font-family: sans-serif; font-weight: bold; }

.hero-box { padding: 40px 20px; text-align: left; }
.manual-image-container { 
  width: 100%; aspect-ratio: 16/9; background: #f0f0f0; border: 4px solid #333; 
  position: relative; overflow: hidden; margin-bottom: 30px;
  box-shadow: inset 0 0 30px rgba(0,0,0,0.1);
}
.manual-bg { width: 100%; height: 100%; object-fit: cover; opacity: 0.9; }
.manual-overlay-graphics { position: absolute; top: 10px; right: 10px; text-align: right; }
.piece-count, .age-label { font-size: 0.6rem; background: #fff; padding: 2px 5px; margin-bottom: 5px; border: 1px solid #333; }

.project-title { font-size: 2.5rem; line-height: 1; margin-bottom: 10px; color: #000; }
.manual-subtitle { font-size: 1rem; color: #0055BF; border-top: 2px solid #eee; padding-top: 10px; }

/* Steps */
.build-step { padding: 80px 30px; position: relative; }
.step-marker {
  position: absolute; top: 30px; left: 30px;
  width: 40px; height: 40px; background: #00A3DA; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-size: 1.2rem; box-shadow: 0 4px 0 #007bb8;
  z-index: 5;
}

.brick-plate { background: #fff; border: 4px solid #333; border-radius: 8px; position: relative; padding: 40px 30px; box-shadow: 10px 10px 0 rgba(0,0,0,0.05); }
.plate-studs { position: absolute; top: -14px; left: 0; width: 100%; display: flex; justify-content: space-around; }
.plate-studs span { width: 30px; height: 18px; background: #fff; border: 4px solid #333; border-bottom: none; border-radius: 50% 50% 0 0; }
.greeting-text { font-size: 1.25rem; line-height: 2; white-space: pre-line; color: #333; }

.floating-brick {
  width: 60px; height: 40px; background: #E3000B; border: 4px solid #333; border-radius: 4px;
  position: absolute; right: 10px; bottom: 10px; transform: rotate(15deg);
  z-index: 10; cursor: pointer;
}

/* Step 2 Gallery */
.instruction-grid-box { border: 4px solid #DBE1E7; padding: 50px 20px 30px; background: #f9f9f9; }
.grid-title { font-size: 1rem; color: #0055BF; margin-bottom: 40px; text-align: center; }
.gallery-bricks-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 30px; }

.photo-brick-assembly { position: relative; }
.assembly-ghost-outline {
  position: absolute; top: 10px; left: 10px; width: 100%; height: 100%;
  border: 4px dashed #ccc; border-radius: 8px; z-index: 1;
}
.real-photo-brick {
  aspect-ratio: 1; background-size: cover; background-position: center;
  border: 4px solid #333; border-radius: 8px; position: relative; z-index: 2;
  background-color: #fff;
  animation: snapDown 4s infinite;
}
.stud-layer { position: absolute; top: -10px; left: 0; width: 100%; display: flex; justify-content: space-around; }
.stud-layer span { width: 15px; height: 10px; background: #fff; border: 4px solid #333; border-bottom: none; border-radius: 50% 50% 0 0; }

.assembly-arrow {
  position: absolute; top: -30px; left: 50%; transform: translateX(-50%);
  width: 2px; height: 40px; background: #E3000B;
}
.assembly-arrow::after {
  content: ''; position: absolute; bottom: 0; left: -4px;
  border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 10px solid #E3000B;
}

@keyframes snapDown {
  0% { transform: translateY(-30px); opacity: 0.5; }
  20% { transform: translateY(0); opacity: 1; }
  100% { transform: translateY(0); opacity: 1; }
}

/* Step 3 Location */
.baseplate-info { background: #33A11D; border: 4px solid #333; border-radius: 8px; padding: 40px 20px; color: #fff;}
.green-studs span { background: #33A11D !important; }
.detail-row { display: flex; gap: 20px; align-items: center; margin-bottom: 25px; }
.icon-brick { font-size: 1.5rem; background: #fff; width: 50px; height: 50px; border-radius: 8px; display: flex; align-items: center; justify-content: center; border: 3px solid #333; color: #333; }
.lbl { color: #FFD500; }

.map-preview { height: 100px; background: rgba(255,255,255,0.1); border: 2px dashed #fff; margin: 30px 0; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; }
.lego-action-btns { display: flex; flex-direction: column; gap: 15px; }
.brick-btn { padding: 15px; text-decoration: none; border: 4px solid #333; border-radius: 8px; text-align: center; color: #fff; box-shadow: 0 5px 0 rgba(0,0,0,0.2); }
.brick-btn.blue { background: #0055BF; }
.brick-btn.green { background: #33A11D; border-color: #fff; }

/* Footer */
.lego-build-footer { padding: 80px 40px; text-align: center; background: #f0f0f0; border-top: 8px solid #DBE1E7; }
.build-complete-stamp { display: inline-block; border: 6px solid #33A11D; color: #33A11D; padding: 10px 20px; font-size: 2rem; transform: rotate(-10deg); margin-bottom: 40px; border-radius: 10px; }
.footer-bricks { display: flex; justify-content: center; gap: 5px; height: 20px; margin-bottom: 20px; }
.b { width: 40px; border-radius: 4px 4px 0 0; }
.r { background: #E3000B; } .y { background: #FFD500; } .b { background: #0055BF; } .g { background: #33A11D; }

/* Modal */
.lego-modal { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: rgba(0,0,0,0.9); z-index: 2000; display: flex; align-items: center; justify-content: center; padding: 20px; }
.modal-brick-case { background: #FFF; padding: 20px; border: 8px solid #333; border-radius: 20px; position: relative; max-width: 450px; width: 100%; }
.modal-studs, .modal-bottom-studs { position: absolute; left: 0; width: 100%; display: flex; justify-content: space-around; }
.modal-studs { top: -20px; }
.modal-bottom-studs { bottom: -20px; transform: rotate(180deg); }
.modal-studs span, .modal-bottom-studs span { width: 50px; height: 25px; background: #fff; border: 6px solid #333; border-bottom: none; border-radius: 25px 25px 0 0; }
.modal-photo { width: 100%; border: 4px solid #eee; margin-top: 10px; border-radius: 8px; }
.close-btn { margin-top: 30px; text-align: center; color: #E3000B; cursor: pointer; }

/* Animation */
.brick-snap-enter-active { animation: brickSnapIn 0.5s; }
@keyframes brickSnapIn {
  0% { transform: scale(0.5) translateY(-200px); opacity: 0; }
  70% { transform: scale(1.1) translateY(0); opacity: 1; }
  100% { transform: scale(1) translateY(0); opacity: 1; }
}
</style>
