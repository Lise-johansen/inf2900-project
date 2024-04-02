import { mount } from '@vue/test-utils';
import LoginPath from '@/components/LoginPath.vue';
import router from '@/router';
import axios from 'axios';

// Mock axios to avoid making real requests
jest.mock('axios');
jest.mock('@/assets/about_us.png', () => 'test-file-stub');
jest.mock('@/assets/logo.png', () => 'test-file-stub');

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
    await wrapper.find('form').trigger('submit');
    await wrapper.vm.$nextTick();

    // Wait for asynchronous operations to complete and look for popup
    await wrapper.vm.$nextTick();
    const popup = wrapper.find('.popup');

    // Assert that popup is displayed
    expect(popup.exists()).toBe(true);

    // Log the HTML content of the popup element
    console.log('Popup Content:', popup.text());

    // Assert that error message is displayed
    expect(popup.find('p').text()).toBe('Invalid username or password. Please try again.');
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
    await wrapper.find('form').trigger('submit');
    await wrapper.vm.$nextTick();

    // Wait for asynchronous operations to complete
    await wrapper.vm.$nextTick();

    // Assert that login event is emitted
    expect(wrapper.emitted('login')).toBeTruthy();
  });
});
