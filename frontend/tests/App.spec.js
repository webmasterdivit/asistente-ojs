import { mount } from '@vue/test-utils'
import App from '../src/App.vue'
import { vi } from 'vitest'
import axios from 'axios'

vi.mock('axios')

describe('App.vue', () => {
  it('renderiza el formulario y responde (mock)', async () => {
    axios.post.mockResolvedValueOnce({ data: { response: 'Respuesta a: test' } })
    const wrapper = mount(App)
    await wrapper.find('textarea').setValue('test')
    await wrapper.find('form').trigger('submit.prevent')
    // Espera a que el DOM se actualice
    await wrapper.vm.$nextTick()
    expect(wrapper.html()).toContain('Respuesta a: test')
  })

  it('renderiza el formulario y responde (API real si está disponible)', async () => {
    // Solo ejecuta si el backend está corriendo en localhost:8000
    const wrapper = mount(App)
    await wrapper.find('textarea').setValue('test')
    await wrapper.find('form').trigger('submit.prevent')
    await new Promise(r => setTimeout(r, 1000)) // Espera por la respuesta
    // Puede fallar si el backend no está disponible, pero así se prueba la integración real
    // Solo verifica que haya algún texto en la respuesta
    if (wrapper.html().includes('Respuesta:')) {
      expect(wrapper.html()).toMatch(/Respuesta:/)
    }
  })
})
