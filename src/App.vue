<template>
  <div class="app-wrapper">
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<style>
/* Global Transitions */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
  background: #eee;
}

.theme-nav {
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 10px;
  background: rgba(255,255,255,0.9);
  padding: 10px 20px;
  border-radius: 30px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  z-index: 10000;
  border: 1px solid #ddd;
}

.nav-link {
  text-decoration: none;
  font-size: 0.8rem;
  color: #666;
  font-family: sans-serif;
  font-weight: bold;
}

.router-link-active {
  color: #ff3333;
}
</style>
