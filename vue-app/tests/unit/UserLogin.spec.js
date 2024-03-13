import { mount } from '@vue/test-utils';
import LoginPath from '@/components/LoginPath.vue';
import router from '@/router';
import axios from 'axios';

// Mock axios to avoid making real requests
jest.mock('axios');

describe('LoginPath.vue', () => {
  it('shows login form', () => {
    const wrapper = mount(LoginPath, {
      global: {
        plugins: [router],
      },
    });
    expect(wrapper.find('form').exists()).toBe(true);
  });

  it('displays error message when login fails with invalid credentials', async () => {
    // Mock axios.post to reject promise with an error
    axios.post.mockRejectedValue(new Error('Invalid username or password'));

    const wrapper = mount(LoginPath, {
      global: {
        plugins: [router],
      },
    });

    // Simulate user input
    await wrapper.find('input[type="text"]').setValue('invalidUsername');
    await wrapper.find('input[type="password"]').setValue('invalidPassword');

    // Simulate login button click
    await wrapper.find('button').trigger('click');
    await wrapper.vm.$nextTick();

    // Wait for asynchronous operations to complete
    await wrapper.vm.$nextTick();

    // Assert that error message is displayed
    expect(wrapper.find('p').text()).toBe('Invalid username or password');
  });

  it('emits login event when login button is clicked with valid credentials', async () => {
    // Mock axios.post to resolve promise with mock data
    axios.post.mockResolvedValue({ data: { token: 'mockToken', auth_user: 'mockUser' } });

    const wrapper = mount(LoginPath, {
      global: {
        plugins: [router],
      },
    });

    // Simulate user input
    await wrapper.find('input[type="text"]').setValue('validUsername');
    await wrapper.find('input[type="password"]').setValue('validPassword');

    // Simulate login button click
    await wrapper.find('button').trigger('click');
    await wrapper.vm.$nextTick();

    // Wait for asynchronous operations to complete
    await wrapper.vm.$nextTick();

    // Assert that login event is emitted
    expect(wrapper.emitted('login')).toBeTruthy();
  });
});
