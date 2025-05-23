import React, { useEffect, useState } from "react";
import axios from "axios";

function CreateStudent() {
  const [userForm, setUserForm] = useState({
    name: "",
    email: "",
    rollno: "",
  });

  const inputsHandler = (e) => {
    setUserForm((prevNext) => ({
      ...prevNext,
      [e.target.name]: e.target.value,
    }));
  };

  console.log(userForm)

  const onSubmit = (e) => {
    e.preventDefault();
    axios
      .post("http://localhost:5000/students/create-student", userForm)
      .then((res) => {
        console.log(res.data);
        setUserForm({
          name: "",
          email: "",
          rollno: "",
          age: "",
          gender: "" ,  // Added later by pranav
        });
      });
  };

  useEffect(() => {}, []);

  return (
    <div>
      <div className="form-wrapper">
        <form onSubmit={onSubmit}>


          <div className="mb-3">
            <label className="form-label">Name</label>
            <input
              type="text"
              className="form-control"
              name="name"
              id="name"
              value={userForm.name}
              onChange={inputsHandler}
            />
          </div>



          {/*  added age and gender */}

    <div className="mb-3">
            <label className="form-label">Age</label>
            <input
              type="text"
              className="form-control"
              name="age"
              id="age"
              value={userForm.age}
              onChange={inputsHandler}
            />
          </div>


          <div className="mb-3">
            <label className="form-label">Gender</label>
            <input
              type="text"
              className="form-control"
              name="gender"
              id="gender"
              value={userForm.gender}
              onChange={inputsHandler}
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              type="text"
              className="form-control"
              name="email"
              id="email"
              value={userForm.email}
              onChange={inputsHandler}
            />
          </div>
          <div className="mb-3">
            <label className="form-label">Roll no.</label>
            <input
              type="text"
              className="form-control"
              name="rollno"
              id="rollno"
              value={userForm.rollno}
              onChange={inputsHandler}
            />
          </div>
          <div className="mb-3">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default CreateStudent;
