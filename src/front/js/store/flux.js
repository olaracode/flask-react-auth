const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      backendUrl: process.env.BACKEND_URL,
      token: "",
    },
    actions: {
      registerUser: async (userData) => {
        try {
          const store = getStore();
          const response = await fetch(`${store.backendUrl}/api/register`, {
            body: JSON.stringify(userData),
            method: "POST",
            headers: {
              "content-type": "application/json",
            },
          });
          const data = await response.json();
          alert(data);
          if (response.status !== 201) {
            return false;
          } else {
            return true;
          }
        } catch (error) {
          console.log(error);
        }
      },
      loginUser: async (userData) => {
        try {
          const store = getStore();
          const response = await fetch(`${store.backendUrl}/api/login`, {
            method: "POST",
            headers: {
              "content-type": "application/json",
            },
            body: JSON.stringify(userData),
          });
          const data = await response.json();
          console.log(data);
          setStore({ token: data.token });
        } catch (error) {
          console.log(error);
        }
      },
      // Use getActions to call a function within a fuction
    },
  };
};

export default getState;
