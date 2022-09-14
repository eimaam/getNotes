// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from 'firebase/firestore'
import { getAuth, GoogleAuthProvider } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDDodwXQVaBoTYbEVgWFgJSuQ69I_GuSEM",
  authDomain: "getnotes001.firebaseapp.com",
  projectId: "getnotes001",
  storageBucket: "getnotes001.appspot.com",
  messagingSenderId: "815126767097",
  appId: "1:815126767097:web:322aca9cb4556893dc8928",
  measurementId: "G-KFCC6C2VCH"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const auth = getAuth(app)
export const database = getFirestore(app);
export const googleProvider = new GoogleAuthProvider()