// script.js
// This script file should be included in all HTML pages
function login() {  
    var user = document.getElementById('username').value;
    var pass = document.getElementById('password').value;
    if((user == '2100140100057' && pass == 'pass') || (user == '2100140100056' && pass == 'pass') || (user == '2100140100052' && pass == 'pass') || (user == '2100140100054' && pass == 'pass') || (user == '2100140100058' && pass == 'pass')  ){
      window.location.assign("mainh.html");
    }
    else{
      alert("Enter the details Complete/Correct");
    }
  }
// Dummy data storage
let teamDetails = [];
let projectDetails = [];
function addTeamDetails() {
  // Implement adding team details functionality (dummy function for now)
  const teamForm = document.getElementById('teamForm');
  const teamData = {
    leaderName: teamForm.leaderName.value,
    leaderRollNo: teamForm.leaderRollNo.value,
    member1Name: teamForm.member1Name.value,
    member1RollNo: teamForm.member1RollNo.value,
    member2Name: teamForm.member2Name.value,
    member2RollNo: teamForm.member2RollNo.value,
    member3Name: teamForm.member3Name.value,
    member3RollNo: teamForm.member3RollNo.value,
  };
  teamDetails.push(teamData);
  alert("Team details added successfully.");
}

function addProjectDetails() {
  // Implement adding project details functionality (dummy function for now)
  const projectForm = document.getElementById('projectForm');
  const projectData = {
    projectName: projectForm.projectName.value,
    projectDomain: projectForm.projectDomain.value,
    guideInfo: projectForm.guideInfo.value,
  };
  projectDetails.push(projectData);

}

function displayGroupData() {
  // Implement displaying data functionality (dummy function for now)
  const displayTable = document.getElementById('displayGroupTable');

  // Display team details
  const teamTable = document.createElement('table');
  teamTable.innerHTML = `
    <tr>
      <th>Leader Name</th>
      <th>Leader Roll No</th>
      <th>Member 1 Name</th>
      <th>Member 1 Roll No</th>
      <th>Member 2 Name</th>
      <th>Member 2 Roll No</th>
      <th>Member 3 Name</th>
      <th>Member 3 Roll No</th>
    </tr>
  `;
  teamDetails.forEach(team => {
    teamTable.innerHTML += `
      <tr>
        <td>${team.leaderName}</td>
        <td>${team.leaderRollNo}</td>
        <td>${team.member1Name}</td>
        <td>${team.member1RollNo}</td>
        <td>${team.member2Name}</td>
        <td>${team.member2RollNo}</td>
        <td>${team.member3Name}</td>
        <td>${team.member3RollNo}</td>
      </tr>
    `;
  });

  // Display project details (similar structure as above)
  // ...

  displayTable.appendChild(teamTable);
}
function displayProjectData() {
    // Implement displaying data functionality (dummy function for now)
    const displayTable = document.getElementById('displayProjectTable');
  
    // Display team details
    const teamTable = document.createElement('table');
    teamTable.innerHTML = `
      <tr>
        <th>Project Name</th>
        <th>Project Domain</th>
        <th>Guide Information</th>
      </tr>
    `;
    teamDetails.forEach(team => {
      teamTable.innerHTML += `
        <tr>
          <td>${team.projectName}</td>
          <td>${team.projectDomain}</td>
          <td>${team.guideInfo}</td>


        </tr>
      `;
    });
  
    // Display project details (similar structure as above)
    // ...
  
    displayTable.appendChild(teamTable);
  }
  