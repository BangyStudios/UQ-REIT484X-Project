import MockAdapter from 'axios-mock-adapter';
import mockedAxios from './mockedAxios'

const Mock = new MockAdapter(mockedAxios);
export default Mock;
