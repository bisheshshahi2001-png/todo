<template>
  <div class="min-h-screen bg-[#e0e5ec] flex items-center justify-center p-6">
    <div
      class="w-full max-w-2xl rounded-3xl p-8 shadow-[12px_12px_24px_#bec3c9,-12px_-12px_24px_#ffffff]"
    >
      <!-- Header -->
      <h1 class="text-4xl font-bold text-center text-gray-700 mb-8">
        Todo Application
      </h1>

      <!-- Add Todo -->
      <div class="flex gap-4 mb-8">
        <input
          v-model="newTodo"
          @keyup.enter="addTodo"
          placeholder="What needs to be done?"
          class="flex-1 px-6 py-4 rounded-full bg-[#e0e5ec] outline-none
          shadow-[inset_6px_6px_12px_#bec3c9,inset_-6px_-6px_12px_#ffffff]"
        />

        <button
          @click="addTodo"
          class="px-6 rounded-full bg-[#e0e5ec] text-indigo-600 font-semibold
          shadow-[6px_6px_12px_#bec3c9,-6px_-6px_12px_#ffffff]
          hover:scale-105 active:shadow-[inset_6px_6px_12px_#bec3c9,inset_-6px_-6px_12px_#ffffff]
          transition"
        >
          Add
        </button>
      </div>

      <!-- Todo List -->
      <!-- Todo List -->
<div
  v-for="todo in todos"
  :key="todo.id"
  class="mb-5 rounded-3xl p-5 bg-[#e0e5ec]
  shadow-[8px_8px_16px_#bec3c9,-8px_-8px_16px_#ffffff]
  flex justify-between items-center"
>
  <div class="flex items-center gap-4 flex-1">
    <input
      type="checkbox"
      :checked="todo.completed"
      @change="toggleTodo(todo)"
      class="w-5 h-5 accent-indigo-600"
    />

    <!-- Inline Edit -->
    <input
      v-if="editingId === todo.id"
      v-model="editTitle"
      @keyup.enter="saveEdit(todo)"
      @keyup.esc="cancelEdit"
      @blur="saveEdit(todo)"
      class="flex-1 px-4 py-2 rounded-full bg-[#e0e5ec] outline-none
      shadow-[inset_4px_4px_8px_#bec3c9,inset_-4px_-4px_8px_#ffffff]"
      autofocus
    />

    <span
      v-else
      :class="[
        'text-lg flex-1',
        todo.completed
          ? 'line-through text-gray-400'
          : 'text-gray-700'
      ]"
    >
      {{ todo.title }}
    </span>
  </div>

  <div class="flex gap-3 ml-4">
    <button
      v-if="editingId !== todo.id"
      @click="startEdit(todo)"
      class="px-4 py-2 rounded-full text-blue-600 bg-[#e0e5ec]
      shadow-[4px_4px_8px_#bec3c9,-4px_-4px_8px_#ffffff]
      hover:scale-105 transition"
    >
      Edit
    </button>

    <button
      v-else
      @click="saveEdit(todo)"
      class="px-4 py-2 rounded-full text-green-600 bg-[#e0e5ec]
      shadow-[4px_4px_8px_#bec3c9,-4px_-4px_8px_#ffffff]
      hover:scale-105 transition"
    >
      Save
    </button>

    <button
      @click="deleteTodo(todo.id)"
      class="px-4 py-2 rounded-full text-red-500 bg-[#e0e5ec]
      shadow-[4px_4px_8px_#bec3c9,-4px_-4px_8px_#ffffff]
      hover:scale-105 transition"
    >
      Delete
    </button>
  </div>
</div>
      <div
        v-if="todos.length === 0"
        class="text-center text-gray-500 mt-10"
      >
        No Todos Yet
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const API = `${import.meta.env.VITE_API_URL}/todos`;

const todos = ref([]);
const newTodo = ref("");
const editingId = ref(null);
const editTitle = ref("");

const getTodos = async () => {
  try {
    const res = await axios.get(API);
    todos.value = res.data;
  } catch (err) {
    console.error(err);
  }
};

const addTodo = async () => {
  if (!newTodo.value.trim()) return;

  try {
    await axios.post(API, {
      title: newTodo.value,
      completed: false,
    });

    newTodo.value = "";
    await getTodos();
  } catch (err) {
    console.error(err);
  }
};

const deleteTodo = async (id) => {
  try {
    await axios.delete(`${API}/${id}`);
    await getTodos();
  } catch (err) {
    console.error(err);
  }
};

const startEdit = (todo) => {
  editingId.value = todo.id;
  editTitle.value = todo.title;
};

const cancelEdit = () => {
  editingId.value = null;
  editTitle.value = "";
};

const saveEdit = async (todo) => {
  if (!editTitle.value.trim()) {
    cancelEdit();
    return;
  }

  try {
    await axios.put(`${API}/${todo.id}`, {
      title: editTitle.value,
      completed: todo.completed,
    });

    editingId.value = null;
    editTitle.value = "";

    await getTodos();
  } catch (err) {
    console.error(err);
  }
};

const toggleTodo = async (todo) => {
  try {
    await axios.put(`${API}/${todo.id}`, {
      title: todo.title,
      completed: !todo.completed,
    });

    await getTodos();
  } catch (err) {
    console.error(err);
  }
};

onMounted( async () => {
  await getTodos();
});
</script>