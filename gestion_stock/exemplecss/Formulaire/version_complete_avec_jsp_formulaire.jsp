<%@page import="java.util.Arrays"%>
<%@page import="java.lang.reflect.Array"%>
<%@page import="java.util.Iterator"%>
<%@include file="/resources/includes/jsptag.jsp" %>
<%@page import="java.util.Map.Entry"%>
<%@page import="java.util.Map"%>
<%@page import="java.util.List"%>
<%@page import="java.util.ArrayList" %>
<%@page import="java.util.Date"%>
<%@page import="java.text.DateFormat"%>
<%@page import="java.text.SimpleDateFormat"%>
<%@page import="fr.gouv.finances.mistral.gestab.dataAccessObject.TableBD"%>

<%	    	
	TableBD table = (TableBD) request.getAttribute("table");
	Map<String,String> tupleReference = (Map<String, String>) request.getAttribute("reference");
	Map<String, String> nomsChamps = table.getNomsChamps();
	Map<String, String> typeChamps = table.getTypeChamp();
	Map<String, List<String>> champsLies = (Map<String,List<String>>) request.getAttribute("champsLies");
	Map<String, Integer> nbColARegrouper = table.getNbColARegrouper();
	Map<String, Integer> formats = table.getFormatColonnes();
	Map<String, String> colonneARegrouper = table.getColonnesARegrouper();
	
	Map<String, String[]> nomsColonnesRegroupees = table.getNomsColonnesRegroupees();
	Map<String, Integer> tailleColonne = table.getTailleColonne();
	
%>
<!DOCTYPE html>
<html lang="fr">
	<head>
		<%@ include file="/resources/includes/declare.jsp" %>
	</head>
	<body>
		<header>
			<title><spring:message code="titre.table"/> <% out.print(table.getLibelleLegacy()); %> - Modifier des enregistrements</title>
		</header>	
		<%@ include file="/resources/includes/header.jsp" %>
	    <%@ include file="/resources/includes/nav.jsp" %>
	    <main id="corps">
	    	<div class="tuile">
		    	
				<h1>Modification d'un enregistrement : <% out.println(table.getLibelleLegacy()); %> - <% out.println(table.getLibelleFonctionnel()); %></h1>

				<form autocomplete="off" method="POST">

					<table class="table table-hovered">
						<%
						List<String> listeColonnesAffichees = table.getColonnesAffichees();
						List<String> listeColonnesIgnorees = table.getColonnesIgnorees();
						List<String> listeColonnes = new ArrayList<String>();
						listeColonnes.addAll(listeColonnesAffichees);
						//listeColonnes.addAll(listeColonnesIgnorees);
						
						SimpleDateFormat formatter= new SimpleDateFormat("dd/MM/yyyy");
						String dateActuelle = formatter.format(new Date());
						
						for (String champ : listeColonnes)
						{
							if (typeChamps.containsKey(champ))
							{
								String typeChamp = table.getTypeChamp().get(champ);
						%>
								<tr>
								<!-- nom de colonne -->
									<td class="
									<% 
										if (typeChamp.equals("facultatif"))
											out.print("facultatif col-md-3");
										else if (typeChamp.equals("automatique"))
											out.print("automatique col-md-3");
									%>"
									>
										<label>
											<%
											out.print(nomsChamps.get(champ));
											if (typeChamp.equals("obligatoire"))
												out.print(" *");
											%>
										</label>
									</td>
									<td class="col-md-5">
							<%
							//obligatoire à regrouper
									if (colonneARegrouper != null && colonneARegrouper.containsValue(champ))
									{
										int nbCol = nbColARegrouper.get(champ);
										%>
										<div class="form-inline">
										<%
										for (int i = 0; i < nbCol; i++) // on récupère le nombre de caractères que doit faire chaque colonne pour la clé
										{ 
										%>
										
											<input required class="form-control case chiffres <% out.print(champ); %>" onchange="typageInput(<% out.print(champ); %>)" type="text" maxlength="<% out.print(formats.get(nomsColonnesRegroupees.get(champ)[i])); %>" name="<% out.print(champ); %>[]"/>	
											
										<%
										}
										%>
											
										</div>
										<div id="avertissementTypage"></div>
										<%
									}
							//cas particuliers
									else if (champ.equals("date_validite_poste"))
									{
										out.println("<input class='form-control' type='text' id='datepicker' value='"+ tupleReference.get(champ) +"' name='"+ champ +"' placeholder='Cliquez sur la barre de saisie pour choisir la date'/>");
									}
									else if (champ.equals("code_etat_enrgt"))
									{
									%>
										<input class="form-control" id="disabledInput" name="<% out.print(champ); %>" type="text" value="M" placeholder="M" readonly/>
									<%
									}
									else if (champ.equals("numero_maj_non_concurrence")) // on incrémente de 1 à chaque nouvelle mise à jour
									{
									%>
										<input class="form-control" id="disabledInput" name="<% out.print(champ); %>" type="text" value="<% out.print(tupleReference.get(champ+1)); %>" readonly/>
									<%
									}
									else if (champ.equals("date_derniere_mise_ajour"))
									{
										out.print("<input class='form-control' id='disabledInput' value='"+ dateActuelle +"' name='" +champ+"'type='text' placeholder='" + dateActuelle + "' readonly/>");
									}
									else if (typeChamp.equals("obligatoire") && !table.getValeursPossibles().get(champ).isEmpty())
									{
										boolean inputSansValeurPredefinie = true;
										for (String val : table.getValeursPossibles().get( champ ))
										{
											if(val.equals(tupleReference.get(champ)))
											{										
												out.println("<input autocomplete='off' required list='" + champ + "' value='"+ val +"' class='form-control minimal inputDatalist' name='" + champ + "'/>");
												inputSansValeurPredefinie = false;
											}
										}
										if(inputSansValeurPredefinie)
										{
											out.println("<input autocomplete='off' required list='" + champ + "' class='form-control minimal inputDatalist' name='" + champ + "'/>");
										}

										out.print("<datalist id='" + champ + "' name='" + champ + "'>");	
										for (String val : table.getValeursPossibles().get(champ))
										{
											out.print("<option value='"+ val + "'>" + val + "</option>");
										}
										out.print("</datalist>");

									}
									else
									{
										if (typeChamp.equals("facultatif") || typeChamp.equals("obligatoire"))
										{
											if (champsLies.containsKey(champ)) 
											{
												boolean inputSansValeurPredefinie = true;
												for (String val : champsLies.get(champ))
												{
													if(val.equals(tupleReference.get(champ)))
													{
														out.println("<input autocomplete='off' required list='" + champ + "' value='"+ val +"' class='form-control minimal inputDatalist2' name='" + champ + "'/>");
														inputSansValeurPredefinie = false;
													}
												}
												if(inputSansValeurPredefinie)
												{
													out.println("<input autocomplete='off' required list='" + champ + "' class='form-control minimal inputDatalist2' name='" + champ + "'/>");
												}
												out.print("<datalist id='" + champ + "' name='" + champ + "'>");	
												for (String val : champsLies.get(champ))
												{
													out.print("<option value='"+ val + "'>" + val + "</option>");
												}
												out.print("</datalist>");
											}
											else
											{
										%>
											<input name="<% out.print(champ); %>" <% if(typeChamp.equals("obligatoire")) out.print("required");%> value="<% out.print(tupleReference.get(champ)); %>" class="form-control" type="text" maxlength="<% out.print(tailleColonne.get(champ)); %>" placeholder="Saisissez la valeur du champ <% out.print(nomsChamps.get(champ)); %>"/>
										<%
											}
										}
										else if (typeChamp.equals("automatique"))
										{
											if (champsLies.containsKey(champ))
											{
												boolean inputSansValeurPredefinie = true;
												for (String val : champsLies.get(champ))
												{
													if(val.equals(tupleReference.get(champ)))
													{
														out.println("<input autocomplete='off' value='"+ val +"' list='" + champ + "' class='form-control minimal inputDatalist3' name='" + champ + "'/>");
														
														inputSansValeurPredefinie = false;
													}
												}
												if(inputSansValeurPredefinie)
												{
													out.println("<input autocomplete='off' list='" + champ + "' class='form-control minimal inputDatalist3' name='" + champ + "'/>");
												}
												
												out.print("<datalist id='" + champ + "' name='" + champ + "'>");	
												for (String val : champsLies.get(champ))
												{
													out.print("<option value='"+ val + "'>" + val + "</option>");
												}
												out.print("</datalist>");

											}
											else
											{
										%>
											<input class="form-control" id="disabledInput" name="<% out.print(champ); %>" type="text" placeholder="<%out.println(table.getValeursDefaut().get(champ));%>" readonly/>
										<%
											}
										}
									}
									%>
									</td>
								</tr>
						<%
							}
						}
						%>
						</table>
						
					<button class="btn btn-default">Valider</button>
					
					<a href="<% out.print(request.getContextPath() + "/tables/" + table.getLibelleLegacy());%>" class="btn btn-default">Annuler</a>
				</form>
				
		</main>
		<%@ include file="/resources/includes/footer.jsp" %>
		<%@ include file="/resources/includes/scriptJS.jsp" %>
	</body>
</html>