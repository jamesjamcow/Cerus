import type { Project, CreateProjectPayload } from "../types/type";
import axios from "axios";

import { Project, CreateProjectPayload } from "./types";

const BASE_URL = "http://localhost:8000/api";

export async function fetchAllProjects(): Promise<Project[]> {
  const response = await axios.get(`${BASE_URL}/projects/get_all`);
  if (!response.ok) {
    throw new Error(`Failed to fetch projects: ${response.statusText}`);
  }
  return response.json();
}

export async function createProject(
  payload: CreateProjectPayload
): Promise<Project> {
  const response = await fetch(`${BASE_URL}/projects`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (!response.ok) {
    throw new Error(`Failed to create project: ${response.statusText}`);
  }
  return response.json();
}