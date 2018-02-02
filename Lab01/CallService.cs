using.System.Collections;
using.System.Collections.Generic;
using UnityEngine;

public class CallService : MonoBehaviour {
  // Use this for initialization
  void Start () {
    GetRequest ();
  }
  // https://jsonplaceholder.typicode.com/users
  void GetRequest () {
    string url = "https://jsonplaceholder.typicode.com/users"
    WWW www = new WWW(url);
    StartCoroutine (WaitForRequest(www));
  }
  
  IEnumerator WaitForRequest (WWW www) {
    yield return www;
    
    Debug.Log (www.text);
  }
}
